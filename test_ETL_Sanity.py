import pytest
import pandas as pd

# test if there is any duplicate record
def test_CheckDuplicate():
    target_df = pd.read_csv('target.csv',sep=",")
    count = target_df.duplicated().sum()
    assert count == 0, "Duplicate found"

# test target is not blank
def test_DataCompleteness():
    target_df = pd.read_csv('target.csv')
    assert not target_df.empty,"Target file is empty"

# test if emp_id is mandatory
def test_Emp_id_for_null_value_check():
    target_df = pd.read_csv('target.csv')
    isEmpIdNoNull = target_df['Employee_id'].isnull().any()
    assert isEmpIdNoNull == False,"Employee_id having null value"
