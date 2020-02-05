
# -*- coding: utf-8 -*-
#:include main.kv
import sqlite3 as sql
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivymd.theming import ThemeManager
from kivy.properties import ObjectProperty, BooleanProperty, ListProperty, StringProperty
from kivy.uix.image import Image
from kivy.core.camera import Camera as CoreCamera

conn = sql.connect('user.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS photos(title text, decription text )')

def data_entry():
    c.execute("INSERT INTO photos VALUES('healthy', 'fully healthy beans')")
    conn.commit()
    c.close()
    conn.close()
#class Container(BoxLayout):
def get_data1():
    c.execute('SELECT * FROM photos')
    data = c.fetchall()
    for row in data:
        print(row)
    conn.commit()

def find_data():
    get_data1()
        

    c.close()
    conn.close()
    

class MainApp(App):
    theme_cls = ThemeManager()
    #Container()
    #create_table()
    #data_entry()
    find_data()
    
MainApp().run()