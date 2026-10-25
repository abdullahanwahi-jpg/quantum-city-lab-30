import math
import pytest
from models import MODULES, calculate

def test_all_30_defaults():
    assert len(MODULES)==30
    assert [m.id for m in MODULES]==list(range(1,31))
    for m in MODULES:
        result=calculate(m.id,[x[1] for x in m.inputs])
        assert math.isfinite(result)

def test_historical_rates():
    assert calculate(2,[1000,.265])==pytest.approx(73.5)
    assert calculate(5,[1000,.008])==pytest.approx(99.2)

def test_emissions():
    assert calculate(16,[500,300,1200])==2000
    assert calculate(17,[500000,.4])==200
    assert calculate(18,[1000,.15,.25])==637.5

def test_validation():
    with pytest.raises(ValueError): calculate(19,[100,0.1,50,1000])
    with pytest.raises(ValueError): calculate(1,[1000,0.9])

def test_sensors():
    assert calculate(21,[10,1])==pytest.approx(20)
    assert calculate(22,[1e6,.03,1e6])==pytest.approx(1e9*1e6/(28e9*.03*1000))
    assert calculate(23,[74,74])==pytest.approx(1)
    assert calculate(24,[1000000,.2])==pytest.approx(100/math.sqrt(200000))
    assert calculate(25,[50,12,1.25])==pytest.approx(750)

def test_photonics():
    assert calculate(26,[25,.2,1])==pytest.approx(100*10**(-.6))
    assert calculate(27,[1e6,.5,.8])==pytest.approx(400000)
    assert calculate(28,[100,10])==pytest.approx(100*90/110)
    assert calculate(29,[1e6,.02,.5])==pytest.approx(10000)
    assert calculate(30,[10,3,2])==pytest.approx(10*10**(-.5))
    with pytest.raises(ValueError): calculate(28,[10,100])
