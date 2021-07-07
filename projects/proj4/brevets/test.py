import acp_times
import nose
import arrow

def test_200():
    #Test for 0-200
    date = arrow.Arrow(2020,1,1)
    assert acp_times.open_time(150,200, arrow.get(date)) == (date.shift(hours = 4, minutes = 25)).isoformat()
    assert acp_times.close_time(150, 200, arrow.get(date)) == (date.shift(hours = 10)).isoformat()

def test_311():
    #Test for 200-400
    date = arrow.Arrow(2020,1,1)
    assert acp_times.open_time(311, 400, arrow.get(date)) == (date.shift(hours = 9, minutes = 21)).isoformat()
    assert acp_times.close_time(311, 400, arrow.get(date)) == (date.shift(hours = 20, minutes = 44)).isoformat()

def test_550():
    #Test for 400-600
    date = arrow.Arrow(2020,1,1)
    assert acp_times.open_time(550, 600, arrow.get(date)) == (date.shift(hours = 17, minutes = 8)).isoformat()
    assert acp_times.close_time(550, 600, arrow.get(date)) == (date.shift(hours = 36, minutes = 40)).isoformat()

def test_700():
    #Test for 600-1000
    date = arrow.Arrow(2020,1,1)
    assert acp_times.open_time(700, 1000, arrow.get(date)) == (date.shift(hours = 22, minutes = 22)).isoformat()
    assert acp_times.close_time(700, 1000, arrow.get(date)) == (date.shift(hours = 48, minutes = 45)).isoformat()

def test_same():
    #Test for edge case, same number
    date = arrow.Arrow(2020,1,1)
    assert acp_times.open_time(600, 600, arrow.get(date)) == (date.shift(hours = 18, minutes = 48)).isoformat()
    assert acp_times.close_time(600, 600, arrow.get(date)) == (date.shift(hours = 40)).isoformat()
