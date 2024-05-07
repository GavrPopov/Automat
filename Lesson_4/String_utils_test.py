import pytest
from string_utils import StringUtils
atringutals = StringUtils()

@pytest.mark.parametrize('num1, result', [('text', 'Text'),
                                            ('два слова', 'Два слова'),
                                            ('Go', 'Go'),
                                            ('1,2,3', '1,2,3'),
                                            ('02 мая 2024', '02 мая 2024')])
def test_Capitalize_positive(num1, result):
    test = StringUtils()
    res = test.capitilize(num1)
    assert res == result

@pytest.mark.parametrize('num1, result', [('Два Слова', 'Два Слова'),
                                            (' Go', ' Go'),
                                            ('02 Мая 2024', '02 Мая 2024')])
def test_Capitalize_negative(num1, result):
    test = StringUtils()
    res = test.capitilize(num1)
    assert res == result

@pytest.mark.parametrize('num1, result', [(' text', 'text'),
                                            (' два слова', 'два слова'),
                                            (' 123', '123'),
                                            (' 02 мая 2024', '02 мая 2024')])
def test_Spaces_positive(num1, result):
    test = StringUtils()
    res = test.trim(num1)
    assert res == result

@pytest.mark.parametrize('num1, result', [('  слово  ','  слово  ')])
def test_Spaces_negative(num1, result):
    test = StringUtils()
    res = test.trim(num1)
    assert res == result


@pytest.mark.parametrize('val, delim, result', [('1,2,3', ",",['1','2','3']),
                                                  ('Фамилия,Имя,Отчество', ",",['Фамилия','Имя','Отчество']),
                                                  ('age,heigh,tweight', ",",['age','heigh','tweight']),
                                                  ('Число,Месяц,Год', ",",['Число','Месяц','Год'])])
def test_Delim_count_positive(val, delim, result):
    test = StringUtils()
    res = test.to_list(val, delim)
    assert res == result

@pytest.mark.parametrize('val, delim, result', [(' , , ', "",[' ',' ',' '])])
def test_Delim_count_negative(val, delim, result):
    test = StringUtils()
    res = test.to_list(val, delim)
    assert res == result

@pytest.mark.parametrize('val, sumbol, result', [("Фамилия,Имя,Отчество", "Имя",True),
                                                  ("age,heigh,tweight", "age",True),
                                                  ("1,2,3", "4",False),
                                                  ("Число,Месяц,Год", "age",False)])
def test_Contain_sumbol_positive(val, sumbol, result):
    test = StringUtils()
    res = test.contains(val, sumbol)
    assert res == result

@pytest.mark.parametrize('val, sumbol, result', [("Число,Месяц,Год", "Год",False)])
def test_Contain_sumbol_negaitive(val, sumbol, result):
    test = StringUtils()
    res = test.contains(val, sumbol)
    assert res == result

@pytest.mark.parametrize('val, sumbol, result', [('Фамилия,Имя,Отчество', 'Отчество','Фамилия,Имя,'),
                                                  ('age,heigh,tweight', 'heigh','age,,tweight'),
                                                  ('1,2,3', '1',',2,3')])
def test_Sumbol_del_positive(val, sumbol, result):
    test = StringUtils()
    res = test.delete_symbol(val, sumbol)
    assert res == result

@pytest.mark.parametrize('val, sumbol, result', [('1,2,3', '4',',2,3')])
def test_Sumbol_del_negative(val, sumbol, result):
    test = StringUtils()
    res = test.delete_symbol(val, sumbol)
    assert res == result

@pytest.mark.parametrize('val, sumbol, result', [('Фамилия,Имя,Отчество', 'Фамилия',True),
                                                  ('age,heigh,tweight', 'age',True),
                                                  ('1,2,3', '3',False),
                                                  ('Число,Месяц,Год', 'Год',False)])
def test_Start_check_positive(val, sumbol, result):
    test = StringUtils()
    res = test.starts_with(val, sumbol)
    assert res == result

@pytest.mark.parametrize('val, sumbol, result', [('1,2,3', '1',False),
                                                  ('Число,Месяц,Год', 'Число',False)])
def test_Start_check_negative(val, sumbol, result):
    test = StringUtils()
    res = test.starts_with(val, sumbol)
    assert res == result

@pytest.mark.parametrize('val, sumbol, result', [('Фамилия,Имя,Отчество', 'Отчество',True),
                                                  ('age,heigh,tweight', 'tweight',True),
                                                  ('1,2,3', '1',False),
                                                  ('Число,Месяц,Год', 'Число',False)])
def test_End_check_positive(val, sumbol, result):
    test = StringUtils()
    res = test.end_with(val, sumbol)
    assert res == result

@pytest.mark.parametrize('val, sumbol, result', [('1,2,3', '3',False),
                                                  ('Число,Месяц,Год', 'Год',False)])
def test_End_check_negative(val, sumbol, result):
    test = StringUtils()
    res = test.end_with(val, sumbol)
    assert res == result

@pytest.mark.parametrize('val, result', [('',True),
                                          ('Фамилия', False)])
def test_Str_check_positive(val, result):
    test = StringUtils()
    res = test.is_empty(val)
    assert res == result

@pytest.mark.parametrize('val, result', [('', False)])
def test_Str_check_negative(val, result):
    test = StringUtils()
    res = test.is_empty(val)
    assert res == result

@pytest.mark.parametrize('val, delim, result', [([1,2,3], "*",'1*2*3'),
                                                  ([1,2,3], ";",'1;2;3'),
                                                  ([1,2,3], ":",'1:2:3'),
                                                  ([1,2,3], "#",'1#2#3')])
def test_Str_delim_positive(val, delim, result):
    test = StringUtils()
    res = test.list_to_string(val, delim)
    assert res == result

@pytest.mark.parametrize('val, delim, result', [([1,2,3], "",'1*2*3')])
def test_Str_delim_positive(val, delim, result):
    test = StringUtils()
    res = test.list_to_string(val, delim)
    assert res == result