# Weather decision system
weather = input("What's the weather like? (sunny/rainy/cloudy): ").lower()

if weather == "sunny":
    print("Great day for outdoor activities!")
elif weather == "rainy":
    print("Don't forget your umbrella!")
elif weather == "cloudy":
    print("Might be good for a walk!")
else:
    print("Interesting weather choice!")
