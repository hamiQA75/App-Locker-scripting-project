from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Desired capabilities for the Appium server
capabilities = {
    "appium:deviceName": "950cb2c1",
    "platformName": "Android",
    "automationName": "uiautomator2",
    "appium:app": "C:\\Users\\HamzaAslam\\Downloads\\applocker_vc_22_vn_3.1-debug.apk"
}

appium_server_url = 'http://localhost:4723/wd/hub'

try:
    # Connect to the Appium server
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    wait = WebDriverWait(driver, 20)
    # Wait for the first element to be present and click it
    first_element = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.applock.applocker.lockapps.password.locker:id/btnAgreeX')))
    first_element.click()
    print("First element clicked successfully")

    button_element = None  # Pehle None set karna zaroori hai

    # Pehle XPath se dhundo
    try:
        button_element = wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="Button Text"]'))
        )
    except:
        print("⚠️ XPath button not found, trying CLASS_NAME...")

    # Agar XPath se nahi mila toh CLASS_NAME try karo
    if not button_element:
        try:
            button_element = wait.until(
                EC.presence_of_element_located((AppiumBy.CLASS_NAME, 'android.widget.Button'))
            )
        except:
            print("❌ No button found, moving to next step.")

    # Agar button mila hai toh click karo
    if button_element:
        button_element.click()
        print("✅ Button clicked successfully")
    # Wait for the final element to be present and click it
    final_element = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.applock.applocker.lockapps.password.locker:id/donex')))
    final_element.click()
    print("Final element clicked successfully")

    # Find the "Switch to pin" button by its ID and click it
    switch_to_pin_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.applock.applocker.lockapps.password.locker:id/tvSwitch")))
    switch_to_pin_button.click()
    print("Successfully clicked the 'Switch to pin' button.")

    # Define the IDs for the 4-digit PIN buttons
    pin_button_ids = [
        'com.applock.applocker.lockapps.password.locker:id/key2X',  # ID for digit 2
        'com.applock.applocker.lockapps.password.locker:id/key5X',  # ID for digit 5
        'com.applock.applocker.lockapps.password.locker:id/key8X',  # ID for digit 8
        'com.applock.applocker.lockapps.password.locker:id/key0X'  # ID for digit 0
    ]

    # Function to enter the PIN
    def enter_pin(button_ids):
        for button_id in button_ids:
            pin_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, button_id)))
            pin_button.click()
            print(f"Button with ID '{button_id}' clicked successfully")

    # Enter the PIN for the first time
    enter_pin(pin_button_ids)

    # Enter the PIN for the second time (confirmation)
    enter_pin(pin_button_ids)

    lock_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.applock.applocker.lockapps.password.locker:id/btnLock')))
    lock_button.click()
    print("LOCK button clicked successfully")


    # Function to click on the usage checkbox
    def click_usage_checkbox():
        checkbox_id = "com.applock.applocker.lockapps.password.locker:id/ivUsageCheckboxX"
        try:
            checkbox = wait.until(EC.presence_of_element_located((AppiumBy.ID, checkbox_id)))
            checkbox.click()
            print("Usage checkbox clicked successfully")
        except Exception as e:
            print(f"Failed to click on the usage checkbox: {e}")


    # Call the usage checkbox function at the end
    click_usage_checkbox()


    # Function to click on the confirm button
    def click_confirm_button():
        confirm_button_id = "com.applock.applocker.lockapps.password.locker:id/btnConfirmX"
        try:
            confirm_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, confirm_button_id)))
            confirm_button.click()
            print("Confirm button clicked successfully")
        except Exception as e:
            print(f"Failed to click on the confirm button: {e}")


    # Call the confirm button function
    click_confirm_button()


    def click_app_locker_text():
        app_locker_xpath = "(//android.widget.ImageView[@resource-id='android:id/icon'])[1]"
        try:
            app_locker_element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, app_locker_xpath)))
            app_locker_element.click()
            print("Element with content description 'App Locker' clicked successfully")
        except Exception as e:
            print(f"Failed to click on the element with content description 'App Locker': {e}")

        # Call the function to click "App Locker" element


    click_app_locker_text()


    def click_switch_widget():
        switch_widget_id = "android:id/switch_widget"
        try:
            switch_widget = wait.until(EC.presence_of_element_located((AppiumBy.ID, switch_widget_id)))
            switch_widget.click()
            print("Switch widget clicked successfully")
        except Exception as e:
            print(f"Failed to click on the switch widget: {e}")


    # Call the function to click the switch widget
    click_switch_widget()


    def click_usage_checkbox():
        checkbox_id = "com.applock.applocker.lockapps.password.locker:id/ivDisplayOverCheckboxX"
        try:
            checkbox = wait.until(EC.presence_of_element_located((AppiumBy.ID, checkbox_id)))
            checkbox.click()
            print("Usage checkbox clicked successfully")
        except Exception as e:
            print(f"Failed to click on the usage checkbox: {e}")

        # Call the usage checkbox function at the end


    click_usage_checkbox()


    def click_confirm_button():
        confirm_button_id = "com.applock.applocker.lockapps.password.locker:id/btnConfirmX"
        try:
            confirm_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, confirm_button_id)))
            confirm_button.click()
            print("Confirm button clicked successfully")
        except Exception as e:
            print(f"Failed to click on the confirm button: {e}")

        # Call the confirm button function


    click_confirm_button()


    def click_app_locker_text():
        # Updated XPath (TextView path)
        app_locker_xpath = '(//android.widget.ImageView[@resource-id="android:id/icon"])[1]'

        try:
            # Try to find and click the element using the TextView XPath
            app_locker_element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, app_locker_xpath)))
            app_locker_element.click()
            print("Element with text 'App Locker' clicked successfully")
        except Exception as e:
            print(f"Failed to click on the element with text 'App Locker': {e}")


    # Call the function to click "App Locker" element
    click_app_locker_text()


    def click_switch_widget():
        switch_widget_xpath = '//android.widget.Switch[@resource-id="android:id/switch_widget"]'
        try:
            switch_widget = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, switch_widget_xpath)))
            switch_widget.click()
            print("Switch widget clicked successfully")
        except Exception as e:
            print(f"Failed to click on the switch widget: {e}")

        # Call the function to click the switch widget


    click_switch_widget()


    def click_permission_allow_button():
        # The ID for the 'Allow' permission button
        permission_allow_button_id = "com.android.permissioncontroller:id/permission_allow_button"

        try:
            # Wait for the permission allow button and click it
            permission_allow_button = wait.until(
                EC.presence_of_element_located((AppiumBy.ID, permission_allow_button_id)))
            permission_allow_button.click()
            print("Permission 'Allow' button clicked successfully")
        except Exception as e:
            print(f"Failed to click on the permission 'Allow' button: {e}")


    # Call the function to click the 'Allow' button
    click_permission_allow_button()


    def click_close_button():
        # The ID for the 'Close' button
        close_button_id = "com.applock.applocker.lockapps.password.locker:id/ivCloseX"

        try:
            # Wait for the close button and click it
            close_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, close_button_id)))
            close_button.click()
            print("Close button clicked successfully")
        except Exception as e:
            print(f"Failed to click on the close button: {e}")


    # Call the function to click the 'Close' buttonq2ur dx
    click_close_button()



    def click_intruder_icon():
        """Waits for the 'Intruder' icon to be visible and clicks it using XPath."""
    xpath = "//b[@content-desc='Intruder']"

    try:
        # Wait for the element to be visible before clicking using XPath
        intruder_icon = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, xpath))
        )
        intruder_icon.click()
        print("✅ 'Intruder' icon clicked successfully!")
    except Exception as e:
        print(f"❌ Failed to click the 'Intruder' icon: {e}")

        # Call the function to click the 'Intruder' icon
        click_intruder_icon()


    def click_intruder_switch():
        """Waits for the 'Intruder' switch to be visible and clicks it using ID."""
        element_id = "com.applock.applocker.lockapps.password.locker:id/switchIntruderX"

        try:
            # Wait for the element to be visible before clicking using ID
            intruder_switch = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, element_id))
            )
            intruder_switch.click()
            print("✅ 'Intruder' switch clicked successfully!")
        except Exception as e:
            print(f"❌ Failed to click the 'Intruder' switch: {e}")


    # Call the function to click the 'Intruder' switch
    click_intruder_switch()


    def click_permission_allow_button():
        """Waits for the 'Allow' button to be visible and clicks it using XPath."""
        xpath = "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']"

        try:
            # Wait for the element to be visible before clicking using XPath
            permission_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, xpath))
            )
            permission_button.click()
            print("✅ 'Allow' button clicked successfully!")
        except Exception as e:
            print(f"❌ Failed to click the 'Allow' button: {e}")


    # Call the function to click the 'Allow' button
    click_permission_allow_button()

    # Minimize the app (send it to the background)
    driver.background_app(-1)  # -1 sends the app to the background indefinitely
    print("App sent to the background.")


    def click_page_indicator_caret():
        """Waits for the 'Page Indicator Caret' to be visible and clicks it using ID."""
        element_id = "net.oneplus.launcher:id/page_indicator_caret"

        try:
            # Wait for the element to be visible before clicking using ID
            page_indicator_caret = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, element_id))
            )
            page_indicator_caret.click()
            print("✅ 'Page Indicator Caret' clicked successfully!")
        except Exception as e:
            print(f"❌ Failed to click the 'Page Indicator Caret': {e}")


    # Call the function to click the 'Page Indicator Caret'
    click_page_indicator_caret()


    def click_play_store_text():
        play_store_xpath = '//android.widget.TextView[@content-desc="Play Store"]'

        try:
            # Wait for the Play Store element to be located
            play_store_element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, play_store_xpath)))

            # Click on the Play Store element
            play_store_element.click()
            print("Play Store text clicked successfully.")
        except Exception as e:
            print(f"Failed to click on the Play Store text: {e}")


    click_play_store_text()


    # Function to click a sequence of buttons
    def click_buttons():
        button_ids = [
            'com.applock.applocker.lockapps.password.locker:id/key3',
            'com.applock.applocker.lockapps.password.locker:id/key5',
            'com.applock.applocker.lockapps.password.locker:id/key8',
            'com.applock.applocker.lockapps.password.locker:id/key0'
        ]
        # Click each button one by one
        for button_id in button_ids:
            try:
                button = wait.until(EC.presence_of_element_located((AppiumBy.ID, button_id)))
                button.click()
                print(f"Button with ID '{button_id}' clicked successfully.")
            except Exception as e:
                print(f"Failed to click button with ID '{button_id}': {e}")


    # Call the function to click the buttons
    click_buttons()

    # Minimize the app (send it to the background)
    driver.background_app(-1)  # -1 sends the app to the background indefinitely
    print("App sent to the background.")

    # After the background, click the page indicator caret
    page_indicator_caret = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'net.oneplus.launcher:id/page_indicator_caret')))
    page_indicator_caret.click()
    print("Page indicator caret clicked successfully.")


    # Function definitions
    def click_app_locker_text():
        app_locker_xpath = '//android.widget.TextView[@content-desc=" App Locker"]'

        try:
            app_locker_element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, app_locker_xpath)))
            app_locker_element.click()
            print("Element with content description 'App Locker' clicked successfully")
        except Exception as e:
            print(f"Failed to click on the element with content description 'App Locker': {e}")


    # Call the function to click "App Locker" element
    click_app_locker_text()


    button_element = None  # Pehle None set karna zaroori hai

    # Pehle XPath se dhundo
    try:
        button_element = wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="Button Text"]'))
        )
    except:
        print("⚠️ XPath button not found, trying CLASS_NAME...")

    # Agar XPath se nahi mila toh CLASS_NAME try karo
    if not button_element:
        try:
            button_element = wait.until(
                EC.presence_of_element_located((AppiumBy.CLASS_NAME, 'android.widget.Button'))
            )
        except:
            print("❌ No button found, moving to next step.")

    # Agar button mila hai toh click karo
    if button_element:
        button_element.click()
        print("✅ Button clicked successfully")

    # Function to click a sequence of buttons
    def click_buttons():
        button_ids = [
            'com.applock.applocker.lockapps.password.locker:id/key2X',
            'com.applock.applocker.lockapps.password.locker:id/key5X',
            'com.applock.applocker.lockapps.password.locker:id/key8X',
            'com.applock.applocker.lockapps.password.locker:id/key0X'
        ]
        # Click each button one by one
        for button_id in button_ids:
            try:
                button = wait.until(EC.presence_of_element_located((AppiumBy.ID, button_id)))
                button.click()
                print(f"Button with ID '{button_id}' clicked successfully.")
            except Exception as e:
                print(f"Failed to click button with ID '{button_id}': {e}")


    # Call the function to click the buttons
    click_buttons()




    def click_skip_now():
        skip_now_id = "com.applock.applocker.lockapps.password.locker:id/tvSkipNow"

        try:
            skip_now_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, skip_now_id))
            )
            skip_now_button.click()
            print("Skip Now button clicked successfully.")

        except Exception as e:
            print(f"Failed to click on the Skip Now button: {e}")


    # Call the function to click the "Skip Now" button
    click_skip_now()

    def click_btn_check():
        """Waits for the 'Check' button to be visible and clicks it using ID."""
        element_id = "com.applock.applocker.lockapps.password.locker:id/btnCheck"

        try:
            # Wait for the element to be visible before clicking using ID
            check_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, element_id))
            )
            check_button.click()
            print("✅ 'Check' button clicked successfully!")
        except Exception as e:
            print(f"❌ Failed to click the 'Check' button: {e}")


    # Call the function to click the 'Check' button
    click_btn_check()
    def click_iv_intruder():
     """Waits for the 'Intruder' icon to be visible and clicks it using ID."""
    element_id = "com.applock.applocker.lockapps.password.locker:id/ivIntruder"

    try:
        # Wait for the element to be visible before clicking using ID
        intruder_icon = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.ID, element_id))
        )
        intruder_icon.click()
        print("✅ 'Intruder' icon clicked successfully!")
    except Exception as e:
        print(f"❌ Failed to click the 'Intruder' icon: {e}")

    # Call the function to click the 'Intruder' icon
    click_iv_intruder()


    def click_iv_backx():
        """Waits for the 'Back' icon to be visible and clicks it using ID."""
        element_id = "com.applock.applocker.lockapps.password.locker:id/ivBackx"

        try:
            # Wait for the element to be visible before clicking using ID
            back_icon = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, element_id))
            )
            back_icon.click()
            print("✅ 'Back' icon clicked successfully!")
        except Exception as e:
            print(f"❌ Failed to click the 'Back' icon: {e}")


    # Call the function to click the 'Back' icon
    click_iv_backx()


except Exception as e:
    print(f"❌ An error occurred during execution: {e}")