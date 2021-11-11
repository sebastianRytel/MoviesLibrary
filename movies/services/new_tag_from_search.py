from movies.db.models import MovieTag

def create_new_tag(movie_details):
    added_tags = []
    for tag in movie_details['Genre'].split(','):
        tag_in_db = MovieTag.objects.filter(tag=tag.lower().strip())
        if not tag_in_db:
            new_tag = MovieTag(tag=tag.strip().lower())
            new_tag.save()
            added_tags.append(new_tag.tag)
    return added_tags