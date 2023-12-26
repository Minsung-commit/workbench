# -*- coding: utf-8 -*-

import requests


def get_ntis_data(text):
    
    api_url = "https://www.ntis.go.kr/rndopen/openApi/rcmncls"
    api_key = "h2t9571adb3movumc07l"
    Cd = "0000708"
    coll = ["rcmnitcls", "rcmncls", "rcmnhtcls"]

    
    for c in coll:
    
        # API에 필요한 매개변수 설정
        params = {
            'apprvKey': api_key,
            'orgCd': Cd,
            'collection': c,
            'rqstDes': text,
            # 필요한 다른 매개변수 추가
        }

        try:
            # GET 요청 보내기
            response = requests.get(api_url, params=params)

            # 응답 확인
            response.raise_for_status()

            # 응답 데이터 출력
            print()
            print()
            print(f"컬렉션 명 : {c}")
            print(response.text)
            print()
            print()
        
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

if __name__ == "__main__":

    # text = "이 연구는 스티그머지 통신을 이용한 나노입자와 하이드로겔 결합에 초점을 맞춘 새로운 암 치료 방식을 개발하는 것을 목표로 함. 스티그머지 통신은 나노입자 간의 상호 작용을 통해 특이적인 암 세포를 찾아내고 약물 전달의 정확성을 높일 것으로 기대됨. 본 연구는 발렌시아 폴리테크닉 대학의 Ramon Martinez-Manez 교수와의 협력 하에 이루어지며, 복합적인 기술 결합을 통해 난치성 암에 대한 효과적인 치료 방안을 제시할 것임. 이 연구를 통해 암 치료의 효율과 안전성이 향상되어 환자들의 생존 기간과 삶의 질에 긍정적인 영향을 미칠 것임. 더불어, 본 연구의 결과물은 다양한 암 유형에 대한 치료법 개발에 활용되어 암 연구 전반에 혁신적인 변화를 가져올 것으로 예상됨. 이러한 연구 활동은 암 환자들의 삶의 질 향상과 치료 기술의 발전에 기여하여 암 치료 분야에 중요한 발전을 이룰 것임."
    text = "Presented in this paper is the development of an product cost estimation system in a concurrent, collaborative product development environment. The efficient cost estimation function at the design stage is essential for the cost reduction activities during the entire product life cycle. For this purpose, it is necessary to establish a systematic working procedure, and to develop information system for managing a great deal of production and product-related data required for the cost estimation. The developed system has the capability of estimating a cost of assembly type products as well as unit-item type products. As proposed system is based on the variant approach, it can be used easily at an early design stage without the need for detail design information. Also, this system is integrated with legacy PDM (Product Data Management) and ERP (Enterprise Resource Planning) system for fast, accurate and easy product cost estimation. The estimated cost includes material cost, overhead cost as well as labor cost."
    get_ntis_data(text)
