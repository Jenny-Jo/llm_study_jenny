#########################
# 비즈니스 영역
#########################
import enum
from common.database.call_connector import get_connector
class SQLs(enum.Enum):
    select_actors_by_title = (enum.auto(),"""
    select f1.film_id,
        f1.title,
        count(f2.actor_id) as actor_cnt
    from film f1
    left join film_actor f2
    on f1.film_id = f2.film_id
    group by f1.film_id""", "영화별 배우 수 조회*")


def get_film_list(
    sql_enum = SQLs.select_actors_by_title.name
):
    conn = get_connector()
    sql = SQLs[sql_enum].value[1]
    df = conn.query(sql, ttl=10)
    title = SQLs[sql_enum].value[2]
    return df, title

