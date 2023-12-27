#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""docstring."""
import sys
import wx
from seguid_calculator2.functions import seqfilter
from seguid_calculator2.functions import rc
from seguid_calculator2.functions import slseguid
from seguid_calculator2.functions import scseguid
from seguid_calculator2.functions import dlseguid
from seguid_calculator2.functions import dcseguid
from seguid_calculator2.functions import calcicon
from seguid_calculator2 import __version__

class MyFrame(wx.Frame):
    """doctring."""

    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, -1)
        self.label_2 = wx.StaticText(self.panel_1, -1,
                                     "Raw format only. "
                                     "All characters except A-Z and a-z will be removed.")
        self.slseguid = wx.StaticText(self.panel_1, -1, "slSEGUID")
        self.scseguid = wx.StaticText(self.panel_1, -1, "scSEGUID")
        self.dlseguid = wx.StaticText(self.panel_1, -1, "dlSEGUID")
        self.dcseguid = wx.StaticText(self.panel_1, -1, "dcSEGUID")
        self.size = wx.StaticText(self.panel_1, -1, "Size")
        self.characters = wx.StaticText(self.panel_1, -1, "Characters")

        font = wx.Font(18, wx.MODERN, wx.NORMAL, wx.NORMAL, False,
                       u'Inconsolata')

        self.text_ctrl_slseguid = wx.TextCtrl(self.panel_1, -1, "",
                                            style=wx.TE_READONLY)
        self.text_ctrl_scseguid = wx.TextCtrl(self.panel_1, -1, "",
                                             style=wx.TE_READONLY)
        self.text_ctrl_dlseguid = wx.TextCtrl(self.panel_1, -1, "",
                                             style=wx.TE_READONLY)
        self.text_ctrl_dcseguid = wx.TextCtrl(self.panel_1, -1, "",
                                             style=wx.TE_READONLY)
        self.text_ctrl_size = wx.TextCtrl(self.panel_1, -1, "",
                                          style=wx.TE_READONLY)
        self.text_ctrl_characters = wx.TextCtrl(self.panel_1, -1, "",
                                                style=wx.TE_READONLY)

        # self.text_ctrl_slseguid.Disable()

        self.Calc = wx.Button(self.panel_1, -1, "Calc")
        self.Rev = wx.Button(self.panel_1, -1, "Reverse")
        self.Complement = wx.Button(self.panel_1, -1, "Complement")
        self.rev_comp = wx.Button(self.panel_1, -1, "Reverse complement")
        self.Clear = wx.Button(self.panel_1, -1, "Clear")
        self.text_ctrl_seq = wx.TextCtrl(self.panel_1, -1, "",
                                         style=wx.TE_MULTILINE)

        self.text_ctrl_slseguid.SetFont(font)
        self.text_ctrl_scseguid.SetFont(font)
        self.text_ctrl_dlseguid.SetFont(font)
        self.text_ctrl_dcseguid.SetFont(font)
        self.text_ctrl_size.SetFont(font)
        self.text_ctrl_characters.SetFont(font)
        self.text_ctrl_seq.SetFont(font)

        self.Bind(wx.EVT_BUTTON, self.OnCalc,    self.Calc)
        self.Bind(wx.EVT_BUTTON, self.OnRevComp, self.rev_comp)
        self.Bind(wx.EVT_BUTTON, self.OnCompl,   self.Complement)
        self.Bind(wx.EVT_BUTTON, self.OnRev,     self.Rev)
        self.Bind(wx.EVT_BUTTON, self.OnClear,   self.Clear)

        self.text_ctrl_slseguid.Bind(wx.EVT_SET_FOCUS, self.OnClick)

        self.text_ctrl_seq.SetFocus()

        self.__set_properties()
        self.__do_layout()

        # end wxGlade

    def OnClick(self, event):
        """docstring."""
        self.text_ctrl_slseguid.SetSelection(-1, -1)
        self.text_ctrl_slseguid.SetFocus()

    def OnCalc(self, event):
        """docstring."""
        seq = self.text_ctrl_seq.GetValue()
        filtered_seq = seqfilter(seq)
        self.text_ctrl_slseguid.Clear()
        self.text_ctrl_scseguid.Clear()
        self.text_ctrl_dlseguid.Clear()
        self.text_ctrl_dcseguid.Clear()
        self.text_ctrl_size.Clear()
        self.text_ctrl_seq.Clear()
        if filtered_seq:
            self.text_ctrl_slseguid.SetValue(slseguid(filtered_seq))
            self.text_ctrl_scseguid.SetValue(scseguid(filtered_seq))
            self.text_ctrl_dlseguid.SetValue(dlseguid(filtered_seq))
            self.text_ctrl_dcseguid.SetValue(dcseguid(filtered_seq))
            self.text_ctrl_size.SetValue(str(len(filtered_seq)))
            self.text_ctrl_characters.SetValue(
                " ".join(sorted(set(filtered_seq.upper()))))
            self.text_ctrl_seq.SetValue(filtered_seq)

    def OnRevComp(self, event):
        """docstring."""
        seq = self.text_ctrl_seq.GetValue()
        filtered_seq = rc(seqfilter(seq))
        self.text_ctrl_slseguid.Clear()
        self.text_ctrl_scseguid.Clear()
        self.text_ctrl_dlseguid.Clear()
        self.text_ctrl_dcseguid.Clear()
        self.text_ctrl_size.Clear()
        self.text_ctrl_seq.Clear()
        if filtered_seq:
            self.text_ctrl_slseguid.SetValue(slseguid(filtered_seq))
            self.text_ctrl_scseguid.SetValue(scseguid(filtered_seq))
            self.text_ctrl_dlseguid.SetValue(dlseguid(filtered_seq))
            self.text_ctrl_dcseguid.SetValue(dcseguid(filtered_seq))
            self.text_ctrl_size.SetValue(str(len(filtered_seq)))
            self.text_ctrl_characters.SetValue(
                                   " ".join(sorted(set(filtered_seq.upper()))))
            self.text_ctrl_seq.SetValue(filtered_seq)
        pass

    def OnCompl(self, event):
        """doctstring."""
        seq = self.text_ctrl_seq.GetValue()
        filtered_seq = rc(seqfilter(seq))[::-1]
        self.text_ctrl_slseguid.Clear()
        self.text_ctrl_scseguid.Clear()
        self.text_ctrl_dlseguid.Clear()
        self.text_ctrl_dcseguid.Clear()
        self.text_ctrl_size.Clear()
        self.text_ctrl_seq.Clear()
        if filtered_seq:
            self.text_ctrl_slseguid.SetValue(slseguid(filtered_seq))
            self.text_ctrl_scseguid.SetValue(scseguid(filtered_seq))
            self.text_ctrl_dlseguid.SetValue(dlseguid(filtered_seq))
            self.text_ctrl_dcseguid.SetValue(dcseguid(filtered_seq))
            self.text_ctrl_size.SetValue(str(len(filtered_seq)))
            self.text_ctrl_characters.SetValue(" ".join(
                                            sorted(set(filtered_seq.upper()))))
            self.text_ctrl_seq.SetValue(filtered_seq)
        pass

    def OnRev(self, event):
        """doctstring."""
        seq = self.text_ctrl_seq.GetValue()
        filtered_seq = seqfilter(seq)[::-1]
        self.text_ctrl_slseguid.Clear()
        self.text_ctrl_scseguid.Clear()
        self.text_ctrl_dlseguid.Clear()
        self.text_ctrl_dcseguid.Clear()
        self.text_ctrl_size.Clear()
        self.text_ctrl_seq.Clear()
        if filtered_seq:
            self.text_ctrl_slseguid.SetValue(slseguid(filtered_seq))
            self.text_ctrl_scseguid.SetValue(scseguid(filtered_seq))
            self.text_ctrl_dlseguid.SetValue(dlseguid(filtered_seq))
            self.text_ctrl_dcseguid.SetValue(dcseguid(filtered_seq))
            self.text_ctrl_size.SetValue(str(len(filtered_seq)))
            self.text_ctrl_characters.SetValue(" ".join(
                                            sorted(set(filtered_seq.upper()))))
            self.text_ctrl_seq.SetValue(filtered_seq)
        pass

    def OnClear(self, event):
        """docstring."""
        self.text_ctrl_size.Clear()
        self.text_ctrl_seq.Clear()
        self.text_ctrl_characters.Clear()

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(f"seguid calculator 2 vers {__version__}")
        _icon = calcicon().GetIcon()
        # _icon = wx.EmptyIcon()
        # _icon.CopyFromBitmap(wx.Bitmap(os.path.join(
        # os.path.dirname(__file__),"calc.ico"), wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.text_ctrl_seq.SetMinSize((688, 188))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.label_2, 0, wx.ALL, 5)
        sizer_4.Add(self.slseguid, 0, wx.ALL, 10)
        sizer_4.Add(self.scseguid, 0, wx.ALL, 10)
        sizer_4.Add(self.dlseguid, 0, wx.ALL, 10)
        sizer_4.Add(self.dcseguid, 0, wx.ALL, 10)
        sizer_4.Add(self.size, 0, wx.ALL, 10)
        sizer_4.Add(self.characters, 0, wx.ALL, 10)
        sizer_3.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_5.Add(self.text_ctrl_slseguid, 0, wx.ALL | wx.EXPAND, 5)
        sizer_5.Add(self.text_ctrl_scseguid, 0, wx.ALL | wx.EXPAND, 5)
        sizer_5.Add(self.text_ctrl_dlseguid, 0, wx.ALL | wx.EXPAND, 5)
        sizer_5.Add(self.text_ctrl_dcseguid, 0, wx.ALL | wx.EXPAND, 5)
        sizer_5.Add(self.text_ctrl_size, 0, wx.ALL | wx.EXPAND, 5)
        sizer_5.Add(self.text_ctrl_characters, 0, wx.ALL | wx.EXPAND, 5)
        sizer_3.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 0, wx.EXPAND, 0)
        sizer_6.Add(self.Calc, 0, wx.ALL, 5)
        sizer_6.Add(self.Rev, 0, wx.ALL, 5)
        sizer_6.Add(self.Complement, 0, wx.ALL, 5)
        sizer_6.Add(self.rev_comp, 0, wx.ALL, 5)
        sizer_6.Add(self.Clear, 0, wx.ALL, 5)
        sizer_2.Add(sizer_6, 0, wx.EXPAND, 0)
        sizer_2.Add(self.text_ctrl_seq, 1, wx.ALL | wx.EXPAND, 5)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade


def main():
    """doctring."""
    app = wx.App(0)
    frame_1 = MyFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
