import wx

# Aplicación principal
app = wx.App()

# Ventana
ventana = wx.Frame(None, title="Mi primera ventana", size=(300,200))

def saludar(event):
    wx.MessageBox("hola, wxPython"),
    "Saludo",wx.OK | wx.ICON_INFORMATION
    
# Botón dentro de la ventana
boton = wx.Button(ventana, label="saludar", pos=(100,70))
boton.Bind(wx.EVT_BUTTON,saludar)

# Mostrar ventana
ventana.Show()
app.MainLoop()


