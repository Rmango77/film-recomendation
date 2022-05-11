import pandas as pd
from random import randint
import streamlit as st
from IPython.display import Image

st.title('Система рекомендаций фильмов')

col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.write("")

with col2:
    st.image("/Users/eugeny/Downloads/0*O8OK4ZJtNnakcyQM.jpg")

with col3:
    st.write("")

st.write('')
st.write('')
st.write('Данный стримлит демонстрирует как основываясь на ваших предпочтениях в кино, машинное обучение может порекомендовать максимально релевантный, на ваш вкус, фильм.')
st.markdown("<h1 style='text-align: center; color: black;'>Основная технология</h1>", unsafe_allow_html=True)

st.write('Для построения данной рекомендательной системы были выбраны фильмы и оценки пользователей, предоставленные стриминговым сервисом NETFLIX. При помощи алгоритмов коллаборативной фильтрации (https://ru.wikipedia.org/wiki/Коллаборативная_фильтрация) и метода k ближайших соседей (https://ru.wikipedia.org/wiki/Метод_k-ближайших_соседей) мы получаем рекомендацию из топ 5 фильмов основываясь на его предпочтениях к заранее отобранным фильмам.')
st.markdown("<h1 style='text-align: center; color: black;'>Сбор информации о ваших предпочтениях</h6>", unsafe_allow_html=True)
st.write('Оцените предложенные фильмы или выберете “Не смотрел(а)”')
st.write('')
type_film1 = st.selectbox("История игрушек", [5, 4, 3, 2, 1, "Не смотрел(а)"])
type_film = st.selectbox("Звездные войны", [5, 4, 3, 2, 1, "Не смотрел(а)"])
type_film = st.selectbox("Крестный отец", [5, 4, 3, 2, 1, "Не смотрел(а)"])
type_film = st.selectbox("Титаник", [5, 4, 3, 2, 1, "Не смотрел(а)"])
type_film = st.selectbox("Властелин колец", [5, 4, 3, 2, 1, "Не смотрел(а)"])
type_film = st.selectbox("Назад в будущее", [5, 4, 3, 2, 1, "Не смотрел(а)"])
type_film = st.selectbox("Терминал", [5, 4, 3, 2, 1, "Не смотрел(а)"])
type_film = st.selectbox("Волк с Уолл-стрит", [5, 4, 3, 2, 1, "Не смотрел(а)"])
type_film = st.selectbox("Фарго", [5, 4, 3, 2, 1, "Не смотрел(а)"])
type_film = st.selectbox("Лило и Стич", [5, 4, 3, 2, 1, "Не смотрел(а)"])
if st.button('Подобрать подборку'):
    data = pd.read_csv('/Users/eugeny/Downloads/movie.csv')
    for i in range(5):
        mark = randint(1, 27277)
        st.write(data.loc[mark, 'title'])
    