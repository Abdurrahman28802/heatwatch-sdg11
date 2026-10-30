"""Validate presence and basic consistency of *supplied aggregate* outputs only."""
from pathlib import Path
import csv,json,math,sys
base=Path(__file__).resolve().parents[1]

def csv_rows(name):
    with (base/name).open(encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f))

def nearly(a,b,eps=0.0003):return abs(float(a)-b)<eps

results=[]
val=csv_rows('results/stage5c/taskB_pluto_val_results.csv')
row={r['model']:r for r in val}
for name,expected in [('HistGB | 311 gecmisi',0.8452),('HistGB | 311 + HPD',0.8470),('HistGB | 311 + PLUTO',0.8862)]:
    assert nearly(row[name]['ROC_AUC'],expected),(name,row[name]);results.append(f'{name}: {expected}')
assert len(csv_rows('results/stage6c/s6c_A_rolling.csv'))==4
perm=json.loads((base/'results/stage6c/s6c_D_permutation.json').read_text())
assert nearly(perm['D_permutation_val']['ROC'],0.4464)
pluto=json.loads((base/'results/stage5c/dq_pluto.json').read_text())
assert int(pluto['universe_bbl'])==183417
units=sum(int(r['n']) for r in csv_rows('results/stage5c/eda_pluto_by_units.csv'))
age=sum(int(r['n']) for r in csv_rows('results/stage5c/eda_pluto_by_age.csv'))
assert units==182128 and age==181134
print('PASS: Stage 5C/6C aggregate artifact checks')
print('Historical validation and permutation control are NOT model reproduction.')
print('Units grouped:',units,'(excluded or not represented:',183417-units,')')
print('Age grouped:',age,'(excluded or not represented:',183417-age,')')
for r in results:print('-',r)
