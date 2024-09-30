from modules.argument_manager import ArgumentManager, ArgumentOptions
from modules.file_utils import handle_show_report
from modules.core import Instpector
from modules.session_utils import handle_security_key
from modules.version_manager import check_updates

def main():
    args = ArgumentManager()

    check_updates()
    handle_show_report(user=args.get(ArgumentOptions.SHOW_REPORT))
    handle_security_key(generate_key_arg=args.get(ArgumentOptions.GENERATE_KEY))

    instpector = Instpector(arguments=args)
    instpector.authenticate()
    instpector.get_groups()
    instpector.show_metrics()
    instpector.close()

    print("✅ Done, thanks for using Instpector!")
    print("🌟 Star the project on GitHub", "\n- https://github.com/alefranzoni/instpector")

if __name__ == "__main__":
    main()
