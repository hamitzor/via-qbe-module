from .operation_model import OperationModel
from ..args import parser


args = parser.parse_args()


database_config = dict(
    db_host=args.db_host,
    db_username=args.db_username,
    db_password=args.db_password,
    db_name=args.db_name
)

operation_model = OperationModel(database_config)

result = operation_model.get(1)

print "Operation 1 : ", result


new_values = dict(argv="my argv",
                  result="hellor result",
                  watch_id="hello watcher")

operation_model.update(2, new_values)
