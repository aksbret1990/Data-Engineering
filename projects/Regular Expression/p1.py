

def clean_names(raw_names):
    import re
    try:
        result_list = []
        #this part is to compile the regular expression for legal name or dba name once it has been split
        pattern = re.compile(r'\w[/.\w\s///,-]*\w')
        #iterate over each string in RAW_NAMES list
        for cstring in raw_names:
            #this part is to split legal name and dba name if we get dba like pattern
            splits = re.split(r'\W*[dD]\W*[bB]\W*[aA]\W\W*', cstring)
            #this part is if re.split results in two strings which means dba like pattern found
            if len(splits) > 1:
                #below part is to search legal_name 
                clean_legal_name = pattern.search(splits[0])
                #below part is to actually get legal name
                legal_name = clean_legal_name.group()
                #we just join the words in legal name by a space
                legal_name = ' '.join(legal_name.split())
                #below part is to search dba name 
                clean_dba_name = pattern.search(splits[1])
                #below part is to actually get dba name
                dba_name = clean_dba_name.group()
                #we just join the words in dba name by a space
                dba_name = ' '.join(dba_name.split())
                #below part is to create a tuple and replace underscore with space
                result_tuple = (legal_name.replace("_"," "),dba_name.replace("_"," "))
            #this part is if re.split results one strings which means dba like pattern not found
            else:
                #same steps like above
                clean_legal_name = pattern.search(splits[0])
                legal_name = clean_legal_name.group()
                legal_name = ' '.join(legal_name.split())
                result_tuple = (legal_name.replace("_"," "),None)
            #below we just append the tupple to the actual result list
            result_list.append(result_tuple) 
        return result_list 
    except Exception as e:
        print(str(e))
       
        
        
CLEANED_NAME_PAIRS = [
    ('SPV Inc',                  'Super Company'),
    ('Michael Forsky LLC',       'F/B Burgers'),
    ('Youthful You Aesthetics',  None),
    ('Aruna Indika',             'NGXess'),
    ('Diot SA',                  'Diot-Technologies'),
    ('PERFECT PRIVACY, LLC',     'Perfection'),
    ('PostgreSQL DB Analytics',  None),
    ('JAYE INC',                 None),
    ('ETABLISSEMENTS SCHEPENS',  'ETS SCHEPENS'),
    ('DUIKERSTRAINING OOSTENDE', 'D.T.O')
]

RAW_NAMES = [
    'SPV  Inc., DBA:   Super  Company',
    'Michael Forsky LLC d.b.a F/B Burgers .',
    '*** Youthful You Aesthetics ***',
    'Aruna Indika (dba. NGXess)',
    'Diot SA,  -  D. B. A.   *Diot-Technologies*',
    'PERFECT PRIVACY, LLC, d-b-a Perfection,',
    'PostgreSQL DB Analytics',
    '/JAYE INC/',
    ' ETABLISSEMENTS  SCHEPENS /D.B.A./ ETS_SCHEPENS',
    'DUIKERSTRAINING OOSTENDE | D.B.A.:  D.T.O. '
]

assert clean_names(RAW_NAMES) == CLEANED_NAME_PAIRS