# -*- coding: utf-8 -*-
"""Proyecto Visualizacion de informacion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P9e4PLeOqF1Ru4uO1S9Hv-yXas9Y9j1J

**Alumnos:**
- Roberto Araya
- Felipe Aguirre
- Tomas Vega
"""

import altair as alt
import pandas as pd
import numpy as np
import streamlit as st
from vega_datasets import data 

df1 = pd.read_csv('https://raw.githubusercontent.com/k3lr1c/streamlit/main/UFO_scrubbed.csv')

alt.data_transformers.disable_max_rows()

st.title("UFO Report")


countries = alt.topo_feature(data.world_110m.url, 'countries')

input_dropdown = alt.binding_select(options=['cylinder', 'light', 'circle', 'sphere', 'disk', 'fireball',
       'unknown', 'oval', 'other', 'cigar', 'rectangle', 'chevron',
       'triangle', 'formation', 'delta', 'changing', 'egg',
       'diamond', 'flash', 'teardrop', 'cone', 'cross', 'pyramid',
       'round', 'crescent', 'flare', 'hexagon', 'dome', 'changed'], name='shape')
selection = alt.selection_single(fields=['shape'], bind=input_dropdown)

color_scale = alt.Scale(domain=['M', 'F'],
                        range=['#1FC3AA', '#8624F5'])

background = alt.Chart(countries).mark_geoshape(
    fill='lightgray',
    stroke='white'
).project(
    "equirectangular"
).properties(
    width=800,
    height=500
)

base = alt.Chart(df1).properties(
    width=250,
    height=250
).add_selection(selection)

points = base.mark_circle().encode(
    longitude='longitude :Q',
    latitude='latitude:Q',
    size=alt.value(10),
    tooltip='shape'
).add_selection(
    selection
).transform_filter(
    selection
)


hists = base.mark_bar().encode(
    x='datetime:T',
    y='count(datetime)'
).transform_filter(
    selection
).properties(
    width=800,
    height=500
)

st.altair_chart((background + points | hists), use_container_width=True)
