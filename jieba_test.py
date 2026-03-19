import jieba

def run_test():
    print("--- Docker 镜像内 jieba 分词测试 ---")
    
    # 测试 1: 基础分词模式
    string = "我来到北京清华大学"
    print(f"待处理文本: {string}")
    
    print("精确模式: " + "/".join(jieba.cut(string, cut_all=False)))
    print("全模式: " + "/".join(jieba.cut(string, cut_all=True)))
    print("搜索引擎模式: " + "/".join(jieba.cut_for_search(string)))
    
    # 测试 2: 自定义词典功能
    string2 = "乒乓球拍卖完了吗"
    print(f"\n待处理文本: {string2}")
    print("默认分词: " + "/".join(jieba.cut(string2)))
    
    print("添加自定义词: '乒乓球拍'...")
    jieba.add_word("乒乓球拍", freq=1000)
    print("修改后分词: " + "/".join(jieba.cut(string2)))

if __name__ == "__main__":
    run_test()