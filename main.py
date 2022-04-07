from plyer import notification
import time
if __name__=="__main__":
    while True :
        notification.notify(
            title = "Please Drink Water!",
            message = "Drinking water can prevent dehydration, a condition that result in mood change, cause your body to overheat, and lead to constipation and kidney stones",
            app_icon ="C:\\Users\\shrey\\Desktop\\drink water Notify\\pint.ico",
            timeout=5
        )
        time.sleep(6)