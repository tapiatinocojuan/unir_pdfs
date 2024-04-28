# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 977,294 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_BORDER|wx.SP_LIVE_UPDATE )
		self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )

		self.m_panel1 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid1 = wx.grid.Grid( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 0, 1 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.SetColSize( 0, 589 )
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelValue( 0, u"Archivos" )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer2.Add( self.m_grid1, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bpButton1 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton1.SetBitmap( wx.Bitmap( u"img/up.png", wx.BITMAP_TYPE_ANY ) )
		bSizer3.Add( self.m_bpButton1, 0, wx.ALL, 5 )

		self.m_bpButton2 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton2.SetBitmap( wx.Bitmap( u"img/down.png", wx.BITMAP_TYPE_ANY ) )
		bSizer3.Add( self.m_bpButton2, 0, wx.ALL, 5 )

		self.m_bpButton3 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton3.SetBitmap( wx.Bitmap( u"img/mas.png", wx.BITMAP_TYPE_ANY ) )
		bSizer3.Add( self.m_bpButton3, 0, wx.ALL, 5 )

		self.m_bpButton4 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton4.SetBitmap( wx.Bitmap( u"img/del.png", wx.BITMAP_TYPE_ANY ) )
		bSizer3.Add( self.m_bpButton4, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer3, 0, wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"exportar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		self.m_panel3 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_splitter1.SplitVertically( self.m_panel1, self.m_panel3, 700 )
		bSizer1.Add( self.m_splitter1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_SIZE, self.on_size_change )
		self.m_splitter1.Bind( wx.EVT_SPLITTER_SASH_POS_CHANGED, self.on_sash_changed )
		self.m_bpButton1.Bind( wx.EVT_BUTTON, self.on_up_file )
		self.m_bpButton2.Bind( wx.EVT_BUTTON, self.on_down_file )
		self.m_bpButton3.Bind( wx.EVT_BUTTON, self.on_add_file )
		self.m_bpButton4.Bind( wx.EVT_BUTTON, self.on_del_file )
		self.m_button1.Bind( wx.EVT_BUTTON, self.on_unir )
		self.m_panel3.Bind( wx.EVT_DROP_FILES, self.on_drop_files )
		self.m_panel3.Bind( wx.EVT_PAINT, self.on_paint )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def on_size_change( self, event ):
		event.Skip()

	def on_sash_changed( self, event ):
		event.Skip()

	def on_up_file( self, event ):
		event.Skip()

	def on_down_file( self, event ):
		event.Skip()

	def on_add_file( self, event ):
		event.Skip()

	def on_del_file( self, event ):
		event.Skip()

	def on_unir( self, event ):
		event.Skip()

	def on_drop_files( self, event ):
		event.Skip()

	def on_paint( self, event ):
		event.Skip()

	def m_splitter1OnIdle( self, event ):
		self.m_splitter1.SetSashPosition( 700 )
		self.m_splitter1.Unbind( wx.EVT_IDLE )


