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
    first_element = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.applock.applocker.lockapps.password.locker:id/btnAgreeX')))
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
    final_element = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.applock.applocker.lockapps.password.locker:id/donex')))
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

    def click_vault_element():
        # The XPath for the element with content description "Vault"
        vault_xpath = '//b[@content-desc="Vault"]'
        try:
            # Wait for the element and click it
            vault_element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, vault_xpath)))
            vault_element.click()
            print("Element with content description 'Vault' clicked successfully")
        except Exception as e:
            print(f"Failed to click on the element with content description 'Vault': {e}")

    # Call the function to click the 'Vault' element at the end of the script
    click_vault_element()

    def click_allow_button():
        # The ID for the 'Allow' button
        allow_button_id = "com.applock.applocker.lockapps.password.locker:id/btnAllowX"
        try:
            # Wait for the element and click it
            allow_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, allow_button_id)))
            allow_button.click()
            print("Allow button clicked successfully")
        except Exception as e:
            print(f"Failed to click on the 'Allow' button: {e}")

    # Call the function to click the 'Allow' button at the end of the script
    click_allow_button()

    def click_switch_widget():
        # The ID for the switch widget
        switch_widget_id = "android:id/switch_widget"
        try:
            # Wait for the element and click it
            switch_widget = wait.until(EC.presence_of_element_located((AppiumBy.ID, switch_widget_id)))
            switch_widget.click()
            print("Switch widget clicked successfully")
        except Exception as e:
            print(f"Failed to click on the switch widget: {e}")

    # Call the function to click the switch widget at the end of the script
    click_switch_widget()

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


    def click_floating_button():
        """Waits for the floating button to appear and clicks it."""
        floating_button_id = "com.applock.applocker.lockapps.password.locker:id/ivFloatingBtnX"

        try:
            # Wait for the element and click it
            floating_btn = wait.until(EC.presence_of_element_located((AppiumBy.ID, floating_button_id)))
            floating_btn.click()
            print("✅ Floating button clicked successfully!")
        except Exception as e:
            print(f"❌ Failed to click the floating button: {e}")


    # Call the function to click the floating button at the end of the script
    click_floating_button()


    def click_folder_icon():
        """Waits for the folder icon to appear and clicks it."""
        folder_icon_xpath = "(//android.widget.ImageView[@resource-id='com.applock.applocker.lockapps.password.locker:id/ivFolder'])[1]"

        try:
            # Wait for the element and click it
            folder_icon = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, folder_icon_xpath)))
            folder_icon.click()
            print("✅ Folder icon clicked successfully!")
        except Exception as e:
            print(f"❌ Failed to click the folder icon: {e}")


    # Call the function to click the folder icon at the end of the script
    click_folder_icon()


    def click_folder_icons():
     """Waits for the folder icons to appear and clicks them one by one."""

    folder_icon_xpaths = [
        "(//android.widget.ImageView[@resource-id='com.applock.applocker.lockapps.password.locker:id/ivFolderImage'])[1]",
        "(//android.widget.ImageView[@resource-id='com.applock.applocker.lockapps.password.locker:id/ivFolderImage'])[2]",
        "(//android.widget.ImageView[@resource-id='com.applock.applocker.lockapps.password.locker:id/ivFolderImage'])[3]"
    ]

    try:
        for index, xpath in enumerate(folder_icon_xpaths, start=1):
            folder_icon = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, xpath)))
            folder_icon.click()
            print(f"✅ Folder icon {index} clicked successfully!")

    except Exception as e:
        print(f"❌ Failed to click folder icons: {e}")


    # Call the function to click folder icons one by one
    click_folder_icons()



    def click_hide_button():
        """Waits for the hide button to appear and clicks it."""
    hide_button_id = "com.applock.applocker.lockapps.password.locker:id/btnHideX"

    try:
        # Wait for the element and click it
        hide_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, hide_button_id)))
        hide_button.click()
        print("✅ Hide button clicked successfully!")
    except Exception as e:
        print(f"❌ Failed to click the hide button: {e}")

    # Call the function to click the hide button
    click_hide_button()

    def click_touch_outside():
     """Waits for the 'touch_outside' element to appear and clicks it."""
    touch_outside_id = "com.applock.applocker.lockapps.password.locker:id/touch_outside"

    try:
        # Wait for the element and click it
        touch_outside = wait.until(EC.presence_of_element_located((AppiumBy.ID, touch_outside_id)))
        touch_outside.click()
        print("✅ 'Touch Outside' element clicked successfully!")
    except Exception as e:
        print(f"❌ Failed to click the 'Touch Outside' element: {e}")

    # Call the function to click the 'touch_outside' element
    click_touch_outside()


    def click_vault_icon():
        """Waits for the Vault icon to appear and clicks it."""
    vault_icon_id = "com.applock.applocker.lockapps.password.locker:id/ivVault"

    try:
        # Wait for the element and click it
        vault_icon = wait.until(EC.presence_of_element_located((AppiumBy.ID, vault_icon_id)))
        vault_icon.click()
        print("✅ Vault icon clicked successfully!")
    except Exception as e:
        print(f"❌ Failed to click the Vault icon: {e}")

        # Call the function to click the Vault icon
        click_vault_icon()


    def click_select_all_icon():
        """Waits for the 'Select All' icon to be visible and clicks it using ID."""
        element_id = "com.applock.applocker.lockapps.password.locker:id/ivSelectAllX"

        try:
            # Wait for the element to be visible before clicking using ID
            select_all_icon = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, element_id))
            )
            select_all_icon.click()
            print("✅ 'Select All' icon clicked successfully!")
        except Exception as e:
            print(f"❌ Failed to click the 'Select All' icon: {e}")


    # Call the function to click the 'Select All' icon
    click_select_all_icon()


    def click_hide_button():
        """Waits for the 'Hide' button to be visible and clicks it using ID."""
        element_id = "com.applock.applocker.lockapps.password.locker:id/btnHideX"

        try:
            # Wait for the element to be visible before clicking using ID
            hide_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, element_id))
            )
            hide_button.click()
            print("✅ 'Hide' button clicked successfully!")
        except Exception as e:
            print(f"❌ Failed to click the 'Hide' button: {e}")


    # Call the function to click the 'Hide' button
    click_hide_button()


    def click_confirm_button():
        """Waits for the 'Confirm' button to be visible and clicks it using ID."""
    element_id = "com.applock.applocker.lockapps.password.locker:id/btnConfirmX"

    try:
        # Wait for the element to be visible before clicking using ID
        confirm_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.ID, element_id))
        )
        confirm_button.click()
        print("✅ 'Confirm' button clicked successfully!")
    except Exception as e:
        print(f"❌ Failed to click the 'Confirm' button: {e}")

    # Call the function to click the 'Confirm' button


    click_confirm_button()




except Exception as e:
    print(f"❌ An error occurred during execution: {e}")










