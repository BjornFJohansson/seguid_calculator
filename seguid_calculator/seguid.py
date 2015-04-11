#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
SEGUID calculator
'''

import calc_icon_file
import wx
import string

from _version import get_versions
__version__      = get_versions()['version'][:5]
del get_versions

def seguid(seq):
    import hashlib
    import base64
    m = hashlib.sha1()
    m.update(seq.upper())
    return base64.b64encode( m.digest() ).rstrip("=")

tab = string.maketrans("GATCRYWSMKHBVDNgatcrywsmkhbvdn","CTAGYRWSKMDVBHNctagyrwskmdvbhn")

def rc(s):
    return s.translate(tab)[::-1]

def ChenFoxLyndonBreakpoints(s):
    """Find starting positions of Chen-Fox-Lyndon decomposition of s.
    The decomposition is a set of Lyndon words that start at 0 and
    continue until the next position. 0 itself is not output, but
    the final breakpoint at the end of s is. The argument s must be
    of a type that can be indexed (e.g. a list, tuple, or string).
    The algorithm follows Duval, J. Algorithms 1983, but uses 0-based
    indexing rather than Duval's choice of 1-based indexing.

    Algorithms on strings and sequences based on Lyndon words.
    David Eppstein, October 2011.

    """
    k = 0
    while k < len(s):
        i,j = k,k+1
        while j < len(s) and s[i] <= s[j]:
            i = (s[i] == s[j]) and i+1 or k     # Python cond?yes:no syntax
            j += 1
        while k < i+1:
            k += j-i
            yield k

def ChenFoxLyndon(s):
    """Decompose s into Lyndon words according to the Chen-Fox-Lyndon theorem.
    The arguments are the same as for ChenFoxLyndonBreakpoints but the
    return values are subsequences of s rather than indices of breakpoints.

    Algorithms on strings and sequences based on Lyndon words.
    David Eppstein, October 2011.

    """
    old = 0
    for k in ChenFoxLyndonBreakpoints(s):
        yield s[old:k]
        old = k

def SmallestRotation(s):
    """Find the rotation of s that is smallest in lexicographic order.
    Duval 1983 describes how to modify his algorithm to do so but I think
    it's cleaner and more general to work from the ChenFoxLyndon output.

    Algorithms on strings and sequences based on Lyndon words.
    David Eppstein, October 2011.

    """
    prev,rep = None,0
    for w in ChenFoxLyndon(s+s):
        if w == prev:
            rep += 1
        else:
            prev,rep = w,1
        if len(w)*rep == len(s):
            return w*rep
    raise Exception("Reached end of factorization with no shortest rotation")

def cseguid(seq):
    return seguid( min( SmallestRotation(str(seq)), SmallestRotation(str(rc(seq)))))


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, -1)
        self.label_2 = wx.StaticText(self.panel_1, -1, "Biological sequences only. All except ABCDEFGHIJKLMNOPQRSTUVWXYZ and lowercased will be ignored")
        self.seguid = wx.StaticText(self.panel_1, -1, "SEGUID for sequence")
        self.cseguid = wx.StaticText(self.panel_1, -1, "cSEGUID for sequence")
        self.size = wx.StaticText(self.panel_1, -1, "Size (nucleotides or aa)")
        self.characters = wx.StaticText(self.panel_1, -1, "Characters")

        self.text_ctrl_seguid = wx.TextCtrl(self.panel_1, -1, "", style=wx.TE_READONLY)
        self.text_ctrl_cseguid = wx.TextCtrl(self.panel_1, -1, "", style=wx.TE_READONLY)
        self.text_ctrl_size = wx.TextCtrl(self.panel_1, -1, "", style=wx.TE_READONLY)
        self.text_ctrl_characters = wx.TextCtrl(self.panel_1, -1, "", style=wx.TE_READONLY)
        self.Calc       = wx.Button(self.panel_1, -1, "Calc")
        self.Rev        = wx.Button(self.panel_1, -1, "Reverse")
        self.Complement = wx.Button(self.panel_1, -1, "Complement")
        self.rev_comp   = wx.Button(self.panel_1, -1, "Reverse complement")
        self.Clear      = wx.Button(self.panel_1, -1, "Clear")
        self.text_ctrl_seq = wx.TextCtrl(self.panel_1, -1, "", style=wx.TE_MULTILINE)

        self.Bind(wx.EVT_BUTTON, self.OnCalc,    self.Calc)
        self.Bind(wx.EVT_BUTTON, self.OnRevComp, self.rev_comp)
        self.Bind(wx.EVT_BUTTON, self.OnCompl,   self.Complement)
        self.Bind(wx.EVT_BUTTON, self.OnRev,     self.Rev)
        self.Bind(wx.EVT_BUTTON, self.OnClear,   self.Clear)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def OnCalc(self, event):
        seq=self.text_ctrl_seq.GetValue()
        filtered_seq="".join([base for base in seq if base in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"])
        self.text_ctrl_seguid.Clear()
        self.text_ctrl_cseguid.Clear()
        self.text_ctrl_size.Clear()
        self.text_ctrl_seq.Clear()
        if filtered_seq:
            self.text_ctrl_seguid.SetValue( seguid(filtered_seq.encode()) )
	    self.text_ctrl_cseguid.SetValue( cseguid(filtered_seq.encode()) )
            self.text_ctrl_size.SetValue(str(len(filtered_seq)))
            self.text_ctrl_characters.SetValue(" ".join(sorted(set(filtered_seq.upper()))))
            self.text_ctrl_seq.SetValue(filtered_seq)

    def OnRevComp(self, event):
        seq=self.text_ctrl_seq.GetValue()
        filtered_seq="".join([base for base in seq if base in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"])
        filtered_seq= rc(filtered_seq.encode())
        self.text_ctrl_seguid.Clear()
        self.text_ctrl_cseguid.Clear()
        self.text_ctrl_size.Clear()
        self.text_ctrl_seq.Clear()
        if filtered_seq:
            self.text_ctrl_seguid.SetValue( seguid(filtered_seq.encode()) )
            self.text_ctrl_cseguid.SetValue( cseguid(filtered_seq.encode()) )
            self.text_ctrl_size.SetValue(str(len(filtered_seq)))
            self.text_ctrl_characters.SetValue(" ".join(sorted(set(filtered_seq.upper()))))
            self.text_ctrl_seq.SetValue(filtered_seq)
        pass

    def OnCompl(self, event):
        seq=self.text_ctrl_seq.GetValue()
        filtered_seq="".join([base for base in seq if base in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"])
        filtered_seq= rc(filtered_seq.encode())[::-1]
        self.text_ctrl_seguid.Clear()
        self.text_ctrl_cseguid.Clear()
        self.text_ctrl_size.Clear()
        self.text_ctrl_seq.Clear()
        if filtered_seq:
            self.text_ctrl_seguid.SetValue( seguid(filtered_seq.encode()) )
            self.text_ctrl_cseguid.SetValue( cseguid(filtered_seq.encode()) )
            self.text_ctrl_size.SetValue(str(len(filtered_seq)))
            self.text_ctrl_characters.SetValue(" ".join(sorted(set(filtered_seq.upper()))))
            self.text_ctrl_seq.SetValue(filtered_seq)
        pass

    def OnRev(self, event):
        seq=self.text_ctrl_seq.GetValue()
        filtered_seq="".join([base for base in seq if base in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"])
        filtered_seq= filtered_seq.encode()[::-1]
        self.text_ctrl_seguid.Clear()
        self.text_ctrl_cseguid.Clear()
        self.text_ctrl_size.Clear()
        self.text_ctrl_seq.Clear()
        if filtered_seq:
            self.text_ctrl_seguid.SetValue( seguid(filtered_seq.encode()) )
            self.text_ctrl_cseguid.SetValue( cseguid(filtered_seq.encode()) )
            self.text_ctrl_size.SetValue(str(len(filtered_seq)))
            self.text_ctrl_characters.SetValue(" ".join(sorted(set(filtered_seq.upper()))))
            self.text_ctrl_seq.SetValue(filtered_seq)
        pass


    def OnClear(self, event):
        #self.text_ctrl_seguid.Clear()
        #self.text_ctrl_cseguid.Clear()
        self.text_ctrl_size.Clear()
        self.text_ctrl_seq.Clear()
        self.text_ctrl_characters.Clear()


    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("SEGUID checksum calculator {}".format(__version__))
        _icon = calc_icon_file.calc.getIcon()
        #_icon = wx.EmptyIcon()
        #_icon.CopyFromBitmap(wx.Bitmap(os.path.join(os.path.dirname(__file__),"calc.ico"), wx.BITMAP_TYPE_ANY))
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
        sizer_4.Add(self.seguid, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_4.Add(self.cseguid, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_4.Add(self.size, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_4.Add(self.characters, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_3.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_5.Add(self.text_ctrl_seguid, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_5.Add(self.text_ctrl_cseguid, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_5.Add(self.text_ctrl_size, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_5.Add(self.text_ctrl_characters, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)
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

# end of class MyFrame

def main():
    app = wx.App(0)
    #wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
