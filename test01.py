from main import MyPaddleOCR
 
ocr = MyPaddleOCR()

# 지원 가능한 언어 목록
#ocr.get_available_langs()

#ocr.get_available_models()

img_path = 'assets/images/ocr_test_img.png'
#img_path = 'assets/images/sonamu_T2.jpg'
#img_path = 'assets/images/sonamu_T2_small.png'
#img_path = 'assets/images/minwon_search.png'
ocrtext = ocr.run_ocr(img_path, debug=True)

#ocr.get_ocr_result()