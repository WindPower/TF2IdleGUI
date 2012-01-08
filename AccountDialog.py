import Config
from PyQt4 import QtCore, QtGui

class Ui_AccountDialog(object):
	def __init__(self, AccountDialog, settings, account):
		self.settings = settings
		self.account = account
		self.currentUsername = None
		
		# Create dialog
		self.AccountDialog = AccountDialog
		self.AccountDialog.setObjectName('AccountDialog')
		self.AccountDialog.setWindowModality(QtCore.Qt.NonModal)
		self.AccountDialog.resize(450, 350)
		self.AccountDialog.setMinimumSize(QtCore.QSize(450, 350))
		AccountDialog.setWindowTitle('Account details')
		
		# Add layout widget
		self.gridLayoutWidget = QtGui.QWidget(AccountDialog)
		self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 381, 279))
		self.gridLayoutWidget.setObjectName('gridLayoutWidget')
		
		self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
		self.gridLayout.setMargin(0)
		self.gridLayout.setObjectName('gridLayout')
		
		# Set font for sections
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		
		# Steam account section
		self.label_9 = QtGui.QLabel(self.gridLayoutWidget)
		self.label_9.setFont(font)
		self.label_9.setObjectName('label_9')
		self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
		self.label_9.setText('Steam details')
		
		self.label = QtGui.QLabel(self.gridLayoutWidget)
		self.label.setObjectName('label')
		self.label.setToolTip('Your Steam username')
		self.label.setText('Steam username:')
		self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
		
		self.lineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
		self.lineEdit.setFrame(True)
		self.lineEdit.setObjectName('lineEdit')
		self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
		
		self.label2 = QtGui.QLabel(self.gridLayoutWidget)
		self.label2.setObjectName('label2')
		self.label2.setToolTip('Your Steam password')
		self.label2.setText('Steam password:')
		self.gridLayout.addWidget(self.label2, 2, 0, 1, 1)
		
		self.lineEdit2 = QtGui.QLineEdit(self.gridLayoutWidget)
		self.lineEdit2.setFrame(True)
		self.lineEdit2.setObjectName('lineEdit2')
		self.gridLayout.addWidget(self.lineEdit2, 2, 1, 1, 1)
		
		self.label3 = QtGui.QLabel(self.gridLayoutWidget)
		self.label3.setObjectName('label3')
		self.label3.setToolTip('Your Steam vanity ID')
		self.label3.setText('Steam vanity ID\n(eg. steamcommunity.com/id/<vanityID>):')
		self.gridLayout.addWidget(self.label3, 3, 0, 1, 1)
		
		self.lineEdit3 = QtGui.QLineEdit(self.gridLayoutWidget)
		self.lineEdit3.setFrame(True)
		self.lineEdit3.setObjectName('lineEdit3')
		self.gridLayout.addWidget(self.lineEdit3, 3, 1, 1, 1)
		
		self.label4 = QtGui.QLabel(self.gridLayoutWidget)
		self.label4.setObjectName('label4')
		self.label4.setToolTip('Account nickname')
		self.label4.setText('Account nickname:')
		self.gridLayout.addWidget(self.label4, 4, 0, 1, 1)
		
		self.lineEdit4 = QtGui.QLineEdit(self.gridLayoutWidget)
		self.lineEdit4.setFrame(True)
		self.lineEdit4.setObjectName('lineEdit4')
		self.gridLayout.addWidget(self.lineEdit4, 4, 1, 1, 1)
		
		# Sandboxie section
		self.labelsandboxie = QtGui.QLabel(self.gridLayoutWidget)
		self.labelsandboxie.setFont(font)
		self.labelsandboxie.setObjectName('labelsandboxie')
		self.gridLayout.addWidget(self.labelsandboxie, 5, 0, 1, 1)
		self.labelsandboxie.setText('Sandboxie')
		
		self.label5 = QtGui.QLabel(self.gridLayoutWidget)
		self.label5.setObjectName('label5')
		self.label5.setToolTip('Sandbox name')
		self.label5.setText('Sandbox name:')
		self.gridLayout.addWidget(self.label5, 6, 0, 1, 1)
		
		self.lineEdit5 = QtGui.QLineEdit(self.gridLayoutWidget)
		self.lineEdit5.setFrame(True)
		self.lineEdit5.setObjectName('lineEdit5')
		self.gridLayout.addWidget(self.lineEdit5, 6, 1, 1, 1)
		
		self.label6 = QtGui.QLabel(self.gridLayoutWidget)
		self.label6.setObjectName('label6')
		self.label6.setToolTip('Sandbox path')
		self.label6.setText('Sandbox path:')
		self.gridLayout.addWidget(self.label6, 7, 0, 1, 1)
		
		self.lineEdit6 = QtGui.QLineEdit(self.gridLayoutWidget)
		self.lineEdit6.setFrame(True)
		self.lineEdit6.setObjectName('lineEdit6')
		self.gridLayout.addWidget(self.lineEdit6, 7, 1, 1, 1)
		
		# Other section
		self.labelother = QtGui.QLabel(self.gridLayoutWidget)
		self.labelother.setFont(font)
		self.labelother.setObjectName('labelother')
		self.gridLayout.addWidget(self.labelother, 8, 0, 1, 1)
		self.labelsandboxie.setText('Other')
		
		self.label7 = QtGui.QLabel(self.gridLayoutWidget)
		self.label7.setObjectName('label7')
		self.label7.setToolTip('Groups')
		self.label7.setText('Groups:')
		self.gridLayout.addWidget(self.label7, 9, 0, 1, 1)
		
		self.lineEdit7 = QtGui.QLineEdit(self.gridLayoutWidget)
		self.lineEdit7.setFrame(True)
		self.lineEdit7.setObjectName('lineEdit7')
		self.gridLayout.addWidget(self.lineEdit7, 9, 1, 1, 1)
		
		# Add buttons
		self.buttonBox = QtGui.QDialogButtonBox(AccountDialog)
		self.buttonBox.setGeometry(QtCore.QRect(60, 300, 341, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setCenterButtons(False)
		self.buttonBox.setObjectName('buttonBox')
		
		# Signal connections
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL('accepted()'), self.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL('rejected()'), AccountDialog.reject)
		QtCore.QMetaObject.connectSlotsByName(AccountDialog)

		if self.account:
			self.populateDetails()
	
	def accept(self):
		steam_username = str(self.lineEdit.text())
		steam_password = str(self.lineEdit2.text())
		steam_vanityid = str(self.lineEdit3.text())
		account_nickname = str(self.lineEdit4.text())
		sandbox_name = str(self.lineEdit5.text())
		sandbox_install = str(self.lineEdit6.text())
		groups = str(self.lineEdit7.text())
		
		if steam_username == '':
			QtGui.QMessageBox.warning(self.AccountDialog, 'Error', 'Please enter a Steam username')
		elif steam_password == '':
			QtGui.QMessageBox.warning(self.AccountDialog, 'Error', 'Please enter a Steam password')
		else:
			if steam_vanityid == '': # Try steam username as vanity ID
				steam_vanityid = steam_username
			if groups != '':
				groups_list = groups.replace(' ','').replace('.',',').split(',')
		
			if self.settings.has_section('Account-' + steam_username) and not self.account:
				QtGui.QMessageBox.warning(self.AccountDialog, 'Error', 'Account already exists')
			else:
				if self.currentUsername and self.currentUsername != steam_username:
					self.settings.set_section('Account-' + self.currentUsername)
					self.settings.remove_section()
				self.settings.set_section('Account-' + steam_username)
				if not self.settings.has_section('Account-' + steam_username):
					self.settings.add_section()
				self.settings.set_option('steam_username', steam_username)
				self.settings.set_option('steam_password', steam_password)
				self.settings.set_option('steam_vanityid', steam_vanityid)
				self.settings.set_option('account_nickname', account_nickname)
				self.settings.set_option('sandbox_name', sandbox_name)
				self.settings.set_option('sandbox_install', sandbox_install)
				self.settings.set_option('groups', groups)
				self.AccountDialog.close()
		
	def populateDetails(self):
		self.settings.set_section(self.account)
		self.lineEdit.setText(self.settings.get_option('steam_username'))
		self.lineEdit2.setText(self.settings.get_option('steam_password'))
		self.lineEdit3.setText(self.settings.get_option('steam_vanityid'))
		self.lineEdit4.setText(self.settings.get_option('account_nickname'))
		self.lineEdit5.setText(self.settings.get_option('sandbox_name'))
		self.lineEdit6.setText(self.settings.get_option('sandbox_install'))
		self.lineEdit7.setText(self.settings.get_option('groups'))
		
		self.currentUsername = self.settings.get_option('steam_username')