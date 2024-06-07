Private Sub CommandButton1_Click()
    Dim HJDATA() As Variant
    HJDATA = Array("1-20", "23-40", "41-50") ' 這裡是您的範圍數據

    Dim btnArray(1 To 256) As Variant ' 創建一個256位元的二進位數組
    Dim i As Integer, j As Integer
    Dim rangeParts() As String

    
    Dim startRange As Integer, endRange As Integer


    ' 對於HJDATA中的每個範圍，將範圍內的數組值設為1
    For i = LBound(HJDATA) To UBound(HJDATA)
        rangeParts = Split(HJDATA(i), "-")
        startRange = CInt(rangeParts(0))
        endRange = CInt(rangeParts(1))
        For j = startRange To endRange
            btnArray(j) = j
        Next j
    Next i
    
    '  Call UpdateControllers(btnArray)
 
End Sub


' Function UpdateControllers(btnArray() As Variant)

' End Function