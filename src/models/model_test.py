from .model import Model
from ..args import parser


args = parser.parse_args()


database_config = dict(
    db_host=args.db_host,
    db_username=args.db_username,
    db_password=args.db_password,
    db_name=args.db_name
)

model = Model(database_config)

result = model.get_set_statements(dict(
    a="b",
    c="d",
    e="f",
    g="h"
))

print "get_set_statements : ", result
