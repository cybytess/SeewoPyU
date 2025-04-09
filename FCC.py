import win32api
import win32gui
import win32con
screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
while True:
    try:
        sw = win32gui.FindWindow(None, "希沃管家")
        swf = win32gui.GetForegroundWindow()
        if sw !=0 and sw == swf:
            left, top, right, bottom = win32gui.GetWindowRect(sw)
            if right == screen_width and bottom == screen_height:
                win32gui.SetWindowPos(sw,win32con.HWND_BOTTOM,0,0,0,0,win32con.SWP_HIDEWINDOW | win32con.SWP_NOOWNERZORDER )
                time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
time.sleep(1)

if __name__ == "__main__":
    main()
                        
