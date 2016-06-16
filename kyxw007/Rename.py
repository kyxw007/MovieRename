# coding=utf-8
import jieba
import MovieClient, Utils, SimilarTool


class RenameTool:
    def __init__(self):
        jieba.enable_parallel(4)
        self.client = MovieClient.MovieClient();

    def get_new_filename(self):
        return self.new_filename

    best_movie = None
    best_simlar = 0

    def find_movie_from_key(self, key, file_name):
        print("关键词:", key)
        movieList = self.client.search(key)
        if movieList == 0:
            print("movieList is None")
            return
        for movie in movieList:
            simlar = SimilarTool.similar(movie["title"], movie["original_title"], file_name)
            print(movie["title"], "|", movie["original_title"], "|", simlar)
            if simlar > self.best_simlar:
                self.best_movie = movie
                self.best_simlar = simlar

    def find_fitness_movie(self, file_name):
        self.best_movie = None
        self.best_simlar = 0

        keys = filter(Utils.hasChinese, jieba.cut_for_search(file_name))
        allkey = ""
        for key in keys:
            allkey += key
            self.find_movie_from_key(key, file_name)

        if len(allkey) < 5:
            self.find_movie_from_key(allkey, file_name)
        else:
            self.find_movie_from_key(allkey[0:4], file_name)

        if self.best_simlar != 0:
            self.new_filename = self.best_movie["title"]
            self.new_filename += "." + self.best_movie["original_title"]
            self.new_filename += "." + self.best_movie["year"]
            self.new_filename += ".评分[" + str(self.best_movie["rating"]["average"]) + "]"
            if len(self.best_movie["casts"]) > 0:
                self.new_filename += ".主演[" + self.best_movie["casts"][0]["name"] + "]"
            if len(self.best_movie["directors"]) > 0:
                self.new_filename += ".导演[" + self.best_movie["directors"][0]["name"] + "]"
        else:
            self.new_filename = file_name

        return self.best_movie
