# 선형 리스트 생성 함수
def add_data(data):
    katok.append(None)
    katok[len(katok)-1] = data
    return katok


# data 삽입 함수
def insert_data(data, idx):
    katok.append(None)

    for i in range(len(katok)-1, idx, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[idx] = data


def del_data(data, idx):
    katok[idx] = None

    for i in range(idx+1, len(katok)-1):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[len(katok)-1])


katok = []
