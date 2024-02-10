def compare_texts(text1,text2):

    words1 = text1.split()
    words2 = text2.split()

    common_words = set(words1) & set(words2)
    total_num_common_words = len(common_words)

    total_num_unique_words = len(set(words1 + words2))

    return total_num_common_words / total_num_unique_words


t1 = input("Please type your first piece of text\n")
t2 = input("Please type your second piece of text\n")

similarity_score = compare_texts(t1,t2)
print(f"Similarity score: {similarity_score}")
print("Similarity Percent: {0:2} %".format(similarity_score*100))