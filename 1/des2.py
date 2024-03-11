import io
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MyNotes</class>
 <widget class="QWidget" name="MyNotes">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>355</width>
    <height>374</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>0</width>
    <height>0</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Записная книжка</string>
  </property>
  <widget class="QWidget" name="horizontalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>20</y>
     <width>281</width>
     <height>101</height>
    </rect>
   </property>
   <layout class="QHBoxLayout" name="horizontalLayout">
    <item>
     <layout class="QVBoxLayout" name="verticalLayout">
      <item>
       <widget class="QLabel" name="contactNameText">
        <property name="enabled">
         <bool>true</bool>
        </property>
        <property name="sizePolicy">
         <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
          <horstretch>0</horstretch>
          <verstretch>0</verstretch>
         </sizepolicy>
        </property>
        <property name="text">
         <string>Имя</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLabel" name="contactNumberText">
        <property name="sizePolicy">
         <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
          <horstretch>0</horstretch>
          <verstretch>0</verstretch>
         </sizepolicy>
        </property>
        <property name="text">
         <string>Телефон</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
    <item>
     <layout class="QVBoxLayout" name="verticalLayout_2">
      <item>
       <widget class="QLineEdit" name="contactName"/>
      </item>
      <item>
       <widget class="QLineEdit" name="contactNumber"/>
      </item>
     </layout>
    </item>
    <item>
     <widget class="QPushButton" name="addContactBtn">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Preferred" vsizetype="Fixed">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="text">
       <string>Добавить</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QListWidget" name="contactList">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>150</y>
     <width>281</width>
     <height>181</height>
    </rect>
   </property>
   <property name="contextMenuPolicy">
    <enum>Qt::ActionsContextMenu</enum>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyNotes(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.addContactBtn.clicked.connect(self.add_cont)

    def add_cont(self):
        self.contactList.addItem(
            f'{self.contactName.text()} {self.contactNumber.text()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec_())
