

import re
## parse the data manipulation language and dan define language
## create table
## insert data
## select
## we can use regular expression and we can also use  compiler parser
## as the syntax is not so complex, so we can use regular expression
## how to express invalid syntax, it seems using compiler parser is also good.
## implement a parser according the syntax

## today, writing a basically usable parser
## if we want to support powerful sql, we must use syntax parser
## log framework here?
class Parser():
    def __init__(self):
        self.__pattern_map = {
            'SELECT': r'(SELECT|select) (.*) (FROM|from) (.*)',
            'UPDATE': r'(UPDATE|update) (.*) (SET|set) (.*)',
            'INSERT': r'(INSERT|insert) (INTO|into) (.*) \((.*)\) (VALUES|values) \((.*)\)'
        }

        self.__action_map = {
            'SELECT': self.__select,
            'UPDATE': self.__update,
            'INSERT': self.__insert
        }

    def __filter_space(self, stm):
        return [item for item in stm if item.strip() != ""]

    def __get_comp(self, action):
        return re.compile(self.__pattern_map[action])

    def __insert(self, statement):
        comp = self.__get_comp('INSERT')
        ret = comp.findall(" ".join(statement))
        if ret and len(ret[0]) == 6:
            ret_tmp = ret[0]
            field_data = self.__parse_insert_data(ret_tmp[3], ret_tmp[5])
            if not field_data:
                ## todo log here
                return None
            return {
                'type':'insert',
                'table': ret_tmp[2],
                'fields' : field_data
            }

        else:
            return None
    def __parse_insert_data(self, fields, values):
        if len(fields) != len(values):
            ##todo log here
             return None
        fields = fields.split(",")
        values = values.split(",")
        fields = [e.strip() for e in fields]
        values = [v.strip() for v in values]
        data = {}
        for i in range(len(fields)):
            data[fields[i]]= values[i]
        return data

    def __update(self, statement):
        comp = self.__get_comp('UPDATE')
        ret = comp.findall(" ".join(statement))

        if ret and len(ret[0]) == 4:
            table = ret[0][1]
            update_fields = ret[0][3]
            update_fields = update_fields.split(',')
            filed_map = {}
            for f in update_fields:
                f = f.split("=")
                if len(f) !=2:
                    ##todo log here
                    return None

                filed_map[f[0].strip()] = f[1].strip()

            return {
                'type': 'update',
                'fields': filed_map,
                'table': table
            }
        ##todo  log here
        return None

    def __select(self, statement):
        comp = self.__get_comp('SELECT')
        ret = comp.findall(" ".join(statement))

        if ret and len(ret[0]) == 4:
            fields = ret[0][1]
            table = ret[0][3]

            if fields!= '*':
                fields = [field.strip() for field in fields.split(",")]
            return {
                'type' : 'search',
                'fields': fields,
                'table': table
            }
        return None


    def parse_condition(self, condiction_stm):
        stm = self.__filter_space(condiction_stm)
        return None

    def parse_action(self, action_stm):
        stm = self.__filter_space(action_stm.split(" "))
        action = stm[0].upper()
        return self.__action_map.get(action)(stm)

    def parse(self, statement):
        ## support WHERE
        action_stm, where_stm = None, None
        if "where" in statement:
            stm = statement.split('where')
            action_stm = stm[0]
            where_stm = stm[1]
        else:
            action_stm = statement

        action = self.parse_action(action_stm)

        return action




