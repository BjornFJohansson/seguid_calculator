#from java.io            import *
#from java.lang          import *
from java.awt           import Font,BorderLayout
from javax.swing        import JPanel,JFrame, WindowConstants,BoxLayout, JTextField,JButton,JTextArea,BorderFactory,JScrollPane
from java.lang          import System,Integer


import sha, base64, string

class Example:

  def copyText(self,event):
      rawseq = self._editArea.getText()
      filtered_seq=str("".join([base for base in rawseq if base in "atgcnATGCN"])).upper()
      
      table = string.maketrans("ATGCN","TACGN")
      RC = filtered_seq.upper().translate(table)[::-1]
      SEGUID   = base64.encodestring(sha.new(filtered_seq.upper()).digest()).replace("\n","").rstrip("=")
      SEGUIDRC = base64.encodestring(sha.new(RC).digest()).replace("\n","").rstrip("=")
      
      self._editArea.setText(filtered_seq)
      self.SEGUIDtextfield.text = SEGUID
      self.SEGUIDRCtextfield.text = SEGUIDRC
      self.sizetextfield.text=str(len(self._editArea.getText()))
      
  def clearText(self,event):
      self._editArea.setText("")
      self.sizetextfield.setText("")

  def __init__(self):
        # These lines setup the basic frame, size.
        # the setDefaultCloseOperation is required to completely exit the app
        # when you click the close button
    frame = JFrame("SEGUID checksum calculator for DNA")
    frame.setSize(600, 600)
    frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)

    # Create Panel and add swing components and show it.
    pnl = JPanel()
    
    pnl.layout = BoxLayout(pnl, BoxLayout.Y_AXIS)

    frame.add(pnl)

    self.SEGUIDtextfield = JTextField(27)
    pnl.add(self.SEGUIDtextfield)
    
    self.SEGUIDRCtextfield = JTextField(27)
    pnl.add(self.SEGUIDRCtextfield)
    
    self.sizetextfield = JTextField(27)
    pnl.add(self.sizetextfield)
    
    CalcButton  = JButton('Calc',  actionPerformed=self.copyText)
    ClearButton = JButton('Clear', actionPerformed=self.clearText)
    
    pnl.add(CalcButton)
    pnl.add(ClearButton)
    
    #self.Sequencetextarea = JTextArea(20,50)
    #self.Sequencetextarea=BorderFactory.createEmptyBorder(2,2,2,2)
    #pnl.add(self.Sequencetextarea)
    
    self._editArea = JTextArea(15, 80)
    self._editArea.border=BorderFactory.createEmptyBorder(2,2,2,2)
    self._editArea.font=Font("monospaced", Font.PLAIN, 16)
    self._editArea.lineWrap = True
    #UIManager.setLookAndFeel(SystemLookAndFeel) # ("com.sun.java.swing.plaf.windows.WindowsLookAndFeel")  

    scrollingText = JScrollPane(self._editArea)
    pnl.add(scrollingText, BorderLayout.CENTER)

    frame.pack()
    frame.setVisible(True)

if True: #__name__ == '__main__':
  Example()
