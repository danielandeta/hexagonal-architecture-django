from typing import Optional

from myapp.application.domain.model.identifier.article_id import ArticleId
from myapp.application.domain.model.identifier.user_id import UserId
from myapp.application.domain.model.karma import Karma
from myapp.application.domain.model.vote import Vote
from myapp.application.domain.model.voting_user import ArticleVote, VotingUser
from tests.test_myapp.application.domain.model.identifier.article_id_creation import \
    create_article_id
from tests.test_myapp.application.domain.model.identifier.user_id_creation import \
    create_user_id


def build_voting_user(
    user_id: UserId = None,
    karma: Karma = Karma(10),
    article_vote: Optional[ArticleVote] = None
) -> VotingUser:
    user_id = user_id or create_user_id()

    return VotingUser(user_id, karma, article_vote)


def build_article_vote(
    article_id: ArticleId = None,
    vote: Vote = Vote.UP
) -> ArticleVote:
    article_id = article_id or create_article_id()

    return ArticleVote(
        article_id=article_id,
        vote=vote
    )
