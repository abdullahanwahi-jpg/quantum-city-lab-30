import csv, io, json, os, zipfile
from datetime import datetime, timezone
from pathlib import Path
import streamlit as st
import pandas as pd
from models import MODULES, HISTORICAL, calculate
from book_alignment import ALIGNMENT, CHAPTERS, STEPS

st.set_page_config(page_title='Quantum City Lab | 30 Modules', page_icon='⚛️', layout='wide')
st.title('⚛️ Quantum City Lab')
st.caption('30-program research sandbox · Quantum Computing · Carbon Nanomaterials · Carbon Emissions · Sensors & Diamond Sensors · Quantum Photonics')
st.warning('Research prototype. Unless identified as historical measurements, outputs are illustrative scenarios, not experimentally validated forecasts.')
sections=['All modules','Quantum Computing','Carbon Nanomaterials','Carbon Emissions','Sensors & Diamond Sensors','Quantum Photonics']
section=st.sidebar.selectbox('Research area',sections)
choices=[m for m in MODULES if section=='All modules' or m.section==section]
selected=st.sidebar.selectbox('Choose a program',choices,format_func=lambda m:f'{m.id:02d} — {m.title}')
st.sidebar.markdown('**Security:** Never upload your `.env` or IBM API key. IBM jobs are not submitted by this dashboard.')
st.sidebar.caption('For IBM access, use your separate credential-protected local scripts or an authenticated server-side integration.')

st.subheader(f'Program {selected.id:02d} · {selected.title}')
book=ALIGNMENT[selected.id-1]
with st.expander('📘 Quantum City book connection · urban outcome & pilot',expanded=True):
    st.markdown('**City application:** '+book['city_challenge'])
    st.markdown('**Strategic purpose:** '+book['strategic_role'])
    st.markdown('**Relevant book chapters:** '+book['book_chapters'])
    st.markdown('**Conventional benchmark:** '+book['classical_baseline'])
    st.markdown('**Urban KPIs:** '+book['suggested_kpis'])
    st.markdown('**Evidence status:** '+book['evidence_status'])
    st.caption(book['pilot_requirement'])

st.write(selected.description)
values=[]
cols=st.columns(min(3,len(selected.inputs)))
for i,(label,default,lo,hi,unit) in enumerate(selected.inputs):
    with cols[i%len(cols)]:
        val=st.number_input(f'{label} ({unit})',min_value=float(lo),max_value=float(hi),value=float(default),key=f'{selected.id}_{i}',format='%.6f' if float(default)<1 else '%.3f')
        values.append(val)
try:
    outcome=calculate(selected.id,values)
    st.metric(selected.output, f'{outcome:,.3f} {selected.unit}')
    st.info('Model limitation: '+selected.caveat)
    samples=[]
    variable=selected.inputs[0]
    base=values[0]
    for fraction in [0.5,0.75,1,1.25,1.5]:
        x=max(variable[2],min(variable[3],base*fraction))
        trial=[x]+values[1:]
        try: y=calculate(selected.id,trial)
        except ValueError: continue
        samples.append({'Input '+variable[0]:round(x,6),selected.output:round(y,6)})
    df=pd.DataFrame(samples)
    st.subheader('Scenario sensitivity')
    st.line_chart(df.set_index(df.columns[0]))
    evidence={'created_utc':datetime.now(timezone.utc).isoformat(),'module_id':selected.id,'module':selected.title,'classification':'illustrative simulation','inputs':dict((spec[0],v) for spec,v in zip(selected.inputs,values)),'output':{'name':selected.output,'value':outcome,'unit':selected.unit},'limitations':selected.caveat,'book_alignment':book,'method':'See models.py for reproducible equations','source':'user-supplied parameters and explicit illustrative defaults'}
    csv_bytes=df.to_csv(index=False).encode()
    st.download_button('Download scenario CSV',csv_bytes,file_name=f'program_{selected.id:02d}_scenario.csv',mime='text/csv')
    st.download_button('Download evidence JSON',json.dumps(evidence,indent=2).encode(),file_name=f'program_{selected.id:02d}_evidence.json',mime='application/json')
except ValueError as e:
    st.error(str(e))

st.divider()
st.subheader('Research evidence · Experiments 01–05')
st.caption('Historical observations transcribed from user-shared PowerShell screenshots; not independently retrieved from IBM. Original IBM job records and CSVs should be attached for formal validation.')
with st.expander('View historical experiment data'):
    st.json(HISTORICAL)
    st.download_button('Download historical evidence JSON',json.dumps(HISTORICAL,indent=2).encode(),file_name='historical_experiments_01_05.json',mime='application/json')
    st.bar_chart(pd.DataFrame({'Observed mismatch (%)':[26.5,0.8]},index=['Experiment 02','Experiment 05']))
    st.caption('The 25.7 percentage-point difference is observational, not proof that optimization alone caused the improvement.')

with st.expander('All 30 programs'):
    st.dataframe(pd.DataFrame([{'ID':m.id,'Section':m.section,'Program':m.title,'Output':m.output} for m in MODULES]),hide_index=True,use_container_width=True)

st.divider()
st.header('📘 Quantum City · Book-to-Lab Implementation Framework')
st.write('All 30 programs are mapped to the book’s strategy, readiness, pilot, benchmarking, governance and outcome chapters. The link is an application hypothesis, not a claim of demonstrated quantum advantage.')
st.markdown('**Implementation path:** ' + ' → '.join(STEPS))
st.dataframe(pd.DataFrame(ALIGNMENT)[['program_id','program','category','city_challenge','book_chapters','evidence_status']],hide_index=True,use_container_width=True)
st.download_button('Download complete book-to-program alignment CSV',pd.DataFrame(ALIGNMENT).to_csv(index=False).encode('utf-8-sig'),file_name='quantum_city_book_alignment_30.csv',mime='text/csv')
st.subheader('Urban pilot decision record')
with st.form('pilot_record'):
    owner=st.text_input('Accountable city owner / agency')
    problem=st.text_area('Specific urban problem and intended outcome')
    baseline=st.text_area('Current conventional solution and measured baseline')
    kpi=st.text_input('Primary KPI, target and measurement window')
    source=st.text_input('Dataset provenance / date / permissions')
    risks=st.text_area('Security, privacy, procurement and operational risks')
    decision=st.selectbox('Decision gate',['Not assessed','Data remediation required','Proceed to controlled pilot','Do not proceed','Scale only after independent validation'])
    submitted=st.form_submit_button('Generate pilot record')
if submitted:
    record={'book':'Quantum City: A Practical Guide to Smart-City Strategy, Pilots, Governance and Measurable','program_id':selected.id,'program':selected.title,'book_alignment':book,'accountable_owner':owner,'urban_problem':problem,'classical_baseline':baseline,'target_kpi':kpi,'data_provenance':source,'risks':risks,'gate':decision,'created_utc':datetime.now(timezone.utc).isoformat(),'note':'User-entered plan; not a completed or verified pilot'}
    st.download_button('Download pilot decision record JSON',json.dumps(record,indent=2).encode(),file_name=f'quantum_city_pilot_{selected.id:02d}.json',mime='application/json')
