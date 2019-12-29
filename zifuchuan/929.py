def get_real(email:str):
    ai = email.find('@')
    local = email[:ai]
    jia1 = local.find('+')
    if jia1 != -1:
        local = local[:jia1]
    local = local.replace('.','')  # 使用replace 代替遍历，效率更高
    local += email[ai:]
    return local

print(get_real('111@ppp'))