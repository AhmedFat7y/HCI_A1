#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2010 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##   notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##   notice, this list of conditions and the following disclaimer in
##   the documentation and/or other materials provided with the
##   distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##   the names of its contributors may be used to endorse or promote
##   products derived from this software without specific prior written
##   permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


from PyQt4 import QtCore, QtGui


class MainWindow(QtGui.QWidget):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.set_game_variables()
    self.mainWindowLabel = QtGui.QLabel()
    #self.mainWindowLabel.setSizePolicy(QtGui.QSizePolicy.Expanding,
    #    QtGui.QSizePolicy.Expanding)
    self.mainWindowLabel.setAlignment(QtCore.Qt.AlignCenter)
    self.mainWindowLabel.setStyleSheet("QLabel{font-size: 20px; color: red;}")
    #self.mainWindowLabel.setMinimumSize(240, 160)
    self.mainWindowLabel.setText("Hello world")
    #self.createOptionsGroupBox()
    self.createChoicesLayout()

    mainLayout = QtGui.QVBoxLayout()
    mainLayout.setAlignment(QtCore.Qt.AlignCenter)
    mainLayout.addStretch(3)
    mainLayout.addWidget(self.mainWindowLabel)
    mainLayout.addStretch(4)
    mainLayout.addWidget(self.choicesGroupBox)
    mainLayout.addStretch(3)
    self.setLayout(mainLayout)
    #self.shootScreen()
    #self.delaySpinBox.setValue(5)
    self.showMaximized()
    self.showFullScreen()
    self.setWindowTitle("MainWindow")
    #self.resize(300, 200)

  def resizeEvent(self, event):
    #scaledSize = self.originalPixmap.size()
    #scaledSize.scale(self.mainWindowLabel.size(), QtCore.Qt.KeepAspectRatio)
    #if not self.mainWindowLabel.pixmap() or scaledSize != self.mainWindowLabel.pixmap().size():
    #  self.updateMainWindowLabel()
    pass


  def newMainWindow(self):
    if self.hideThisWindowCheckBox.isChecked():
      self.hide()
    self.newMainWindowButton.setDisabled(True)

    QtCore.QTimer.singleShot(self.delaySpinBox.value() * 1000,
        self.shootScreen)

  """def saveMainWindow(self):
          format = 'png'
          initialPath = QtCore.QDir.currentPath() + "/untitled." + format
      
          fileName = QtGui.QFileDialog.getSaveFileName(self, "Save As",
              initialPath,
              "%s Files (*.%s);;All Files (*)" % (format.upper(), format))
          if fileName:
            self.originalPixmap.save(fileName, format)
      
        def shootScreen(self):
          #if self.delaySpinBox.value() != 0:
          #  QtGui.qApp.beep()
      
          # Garbage collect any existing image first.
          self.originalPixmap = None
          self.originalPixmap = QtGui.QPixmap.grabWindow(QtGui.QApplication.desktop().winId())
          self.updateMainWindowLabel()
      
          self.newMainWindowButton.setDisabled(False)
          #if self.hideThisWindowCheckBox.isChecked():
          #  self.show()
      
        def updateCheckBox(self):
          if self.delaySpinBox.value() == 0:
            self.hideThisWindowCheckBox.setDisabled(True)
          else:
            self.hideThisWindowCheckBox.setDisabled(False)
      
        def createOptionsGroupBox(self):
          self.optionsGroupBox = QtGui.QGroupBox("Options")
      
          self.delaySpinBox = QtGui.QSpinBox()
          self.delaySpinBox.setSuffix(" s")
          self.delaySpinBox.setMaximum(60)
          self.delaySpinBox.valueChanged.connect(self.updateCheckBox)
      
          self.delaySpinBoxLabel = QtGui.QLabel("MainWindow Delay:")
      
          self.hideThisWindowCheckBox = QtGui.QCheckBox("Hide This Window")
      
          optionsGroupBoxLayout = QtGui.QGridLayout()
          optionsGroupBoxLayout.addWidget(self.delaySpinBoxLabel, 0, 0)
          optionsGroupBoxLayout.addWidget(self.delaySpinBox, 0, 1)
          optionsGroupBoxLayout.addWidget(self.hideThisWindowCheckBox, 1, 0, 1, 2)
          self.optionsGroupBox.setLayout(optionsGroupBoxLayout)"""

  def createChoicesLayout(self):
    self.choicesGroupBox = QtGui.QGroupBox("Choices")
    self.buttonsLayout1 = QtGui.QHBoxLayout()
    self.buttonsLayout2 = QtGui.QHBoxLayout()
    for index, available_color in enumerate(self.available_colors):
      choice = self.createButton(available_color,
      self.make_choice(index))
      if index < 4:
        self.buttonsLayout1.addWidget(choice)
      else:
        self.buttonsLayout2.addWidget(choice)

    choiceslayout = QtGui.QVBoxLayout()
    choiceslayout.addLayout(self.buttonsLayout1)
    choiceslayout.addLayout(self.buttonsLayout2)
    self.choicesGroupBox.setLayout(choiceslayout)
  

  def createButton(self, text, member):
    button = QtGui.QPushButton(text)
    button.clicked.connect(member)
    button.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
    button.resize(400, 300)
    return button

  def make_choice(self, choice_number):
    def _make_choice():
      self.choice_number = choice_number
    return _make_choice

  def updateMainWindowLabel(self):
    self.mainWindowLabel.setText("Hello World")

  def set_game_variables(self):
    self.available_colors = ['blue', 'red', 'black', 'magenta', 'yellow', 'green', 'brown', 'white']
    self.user_choice_number = 0
    self.current_choices = []
    self.correct_choice_number = 0

if __name__ == '__main__':

  import sys

  app = QtGui.QApplication(sys.argv)
  mainWindow = MainWindow()
  mainWindow.show()
  sys.exit(app.exec_())
