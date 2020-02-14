import os
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise Exception(
            "USAGE: python make_datafiles.py <articles> <summaries>")
        sys.exit()
    article_dir = sys.argv[1]
    summary_dir = sys.argv[2]

    root_dir = os.path.abspath(os.path.join(article_dir, '..'))
    story_dir = os.path.join(root_dir, "stories")
    if not os.path.exists(story_dir):
        os.makedirs(story_dir)

    articles, summaries = os.listdir(article_dir), os.listdir(summary_dir)
    for idx, s in enumerate(articles):
        article_file = os.path.join(article_dir, "article_%s.txt" % str(idx))
        summary_file = os.path.join(summary_dir, "summary_%s.txt" % str(idx))
        
        article = open(article_file, 'r').read()
        summary = open(summary_file, 'r').read()

        with open(os.path.join(story_dir, "stories_%s.txt" % str(idx)), "w") as file:
            story = article + '\n\n' + '@highlight'+'\n' + summary
            file.write(story)
