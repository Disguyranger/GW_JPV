Sub real_Runner()
    Dim lineA, checkCell As String
    Dim yearlyChange As Double
    Dim lineDate, lineOpen, lineHigh, lineLow, lineClose, lineVol As Long
    Dim counter As Integer
    Dim dict As Object
    'testing the dictionary to see if I can't get it to work
    Set dict = CreateObject("Scripting.Dictionary")
    'Global Variables.
    'meant to check the yearly changes
    yearlyChange = 0
    'checking the column for <Open> (C)
    lineOpen = 0
    'checking the colum for <Close> (F)
    lineClose = 0
    'adding all the <Volume> tab to show Total Stock Volume (G)
    lineVolume = 0
    'Monitoring the Ticker to ensure quality control/correct data placement.
    checkCell = " "
    'Meant to serve as a counter for data placement on lines I-L
    counter = 0
    'The next set will keep the labels, and split them accordingly, writing them to the I1:L1 lines.
    lineA = "Ticker, Yearly Change, Percent Changed, Total Stock Volume"
    splitter = Split(lineA, ", ")
    For i = 1 To 4
        Cells(1, 8 + i) = splitter(i - 1)
    Next i
    'Kept out of worksheet loop so it's only runs once.
    
    For Each ws In Worksheets
        'Last Row will check for the last row of the sheet.
        lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
        
        'This will check each row in the A column and append information as necessary.
        For columnCheck = 2 To lastRow
            If Cells(columnCheck, 1) <> checkCell Then
                checkCell = Cells(columnCheck, 1)
                Cells(counter + 2, 9) = checkCell
                lineOpen = Cells(columnCheck, 3).Value
                counter = counter + 1
                lineVolume = Cells(columnCheck, 6)
            Else
                'call on counter for the Total Volume
                lineVolume = lineVolume + Cells(columnCheck, 7).Value
                Cells(counter + 1, 12).Value = lineVolume

                'Run check to see if following row has same ticker.
                If Cells(columnCheck + 1, 1) <> checkCell Then
                    lineClose = Cells(columnCheck, 6).Value
                    yearlyChange = lineOpen - lineClose
                    ' Will not evaluate iff a 0.
                    If lineOpen = 0 Or lineClose = 0 Then
                        Cells(counter + 1, 11).Value = 0
                        Cells(counter + 1, 10).Value = yearlyChange
                    Else 'runs
                        Cells(counter + 1, 10).Value = yearlyChange
                        Cells(counter + 1, 11).Value = Format(lineOpen / lineClose, "Percent")
                    End If
                End If
            End If
            'Colors cells. Does not color them if no value is in Yearly Change.
            If Cells(columnCheck, 10).Value > 0 Then
                Cells(columnCheck, 10).Interior.Color = RGB(0, 100, 0)
            ElseIf Cells(columnCheck, 10).Value < 0 Then
                Cells(columnCheck, 10).Interior.Color = RGB(255, 0, 0)
            End If
        Next columnCheck
    Next ws
End Sub