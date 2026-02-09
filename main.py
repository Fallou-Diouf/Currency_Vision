import numpy as np
import cv2 as cv
from src.models.detect_and_classify import detect_and_classify
from src.models.compute_total import compute_total

path = "dataset/images/10 cents.jpg"
img = cv.imread(path)
scale = 0.095 
output, results = detect_and_classify(img,scale) 
total = compute_total(results) 
print("Pièces détectées :") 
for coin, d_mm, _ in results: 
    print(f" - {coin} ({d_mm:.2f} mm)") 
print(f"\nSomme totale : {total:.2f} €")
cv.imshow("Coins", output) 
cv.waitKey(0) 
cv.destroyAllWindows()
