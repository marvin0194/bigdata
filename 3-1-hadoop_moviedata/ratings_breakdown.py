from mrjob.job import MRJob
from mrjob.step import MRStep


class RatingsBreakdown(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings)
        ]

    def mapper_get_ratings(self, _, line):
        # TODO add your code here
        (user_id, movie_id, rating, timestamp) = line.split('\t')
        yield rating, 1
        pass

    def reducer_count_ratings(self, key, values):
        # TODO add your code here
        yield key, sum(values)
        pass


if __name__ == '__main__':
    RatingsBreakdown.run()
