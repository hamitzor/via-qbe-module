from .feature_model import FeatureModel
from ..args import parser


args = parser.parse_args()


database_config = dict(
    db_host=args.db_host,
    db_username=args.db_username,
    db_password=args.db_password,
    db_name=args.db_name
)

feature_model = FeatureModel(database_config)

insert_data = []


def frame_no(val):
    if val % 2 is 0:
        return 1
    else:
        return 2


for i in range(1000):
    insert_data.append((i+3, i+5, """Description %s""" % (i,), frame_no(i)))


print """%s features inserted for video %s""" % (
    feature_model.insert_multiple(1, insert_data), 1)

print """%s features in frame %s in video %s""" % (
    len(feature_model.get_multiple(1, 2)), 2, 1)
