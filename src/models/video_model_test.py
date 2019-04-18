from .video_model import VideoModel
from ..args import parser


args = parser.parse_args()


database_config = dict(
    db_host=args.db_host,
    db_username=args.db_username,
    db_password=args.db_password,
    db_name=args.db_name
)

video_model = VideoModel(database_config)

result = video_model.get(2)

print "Video 2 : ", result

new_values = dict(title="New Title2",
                  name="New Name3",
                  fps=20,
                  total_frame_count=100)

video_model.update(2, new_values)
