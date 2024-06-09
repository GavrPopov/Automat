from pages.CalculatorPage import CalculatorPage

def test_calculator(chrome_browser):
    delay = 45
    result = 15
    keys_press = '7+8='

    calc = CalculatorPage(chrome_browser)
    calc.open()
    calc.set_delay(delay)
    calc.input_text(keys_press)
    calc.wait_result(delay, result)

    assert calc.result_text() == str(result)
    