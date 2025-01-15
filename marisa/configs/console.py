from rich.text import TextType
from rich.console import Console as RichConsole


class Console(RichConsole):
    def __init__(self, console: RichConsole = RichConsole(), *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.console = console

    def info(self, content: str, *args, **kwargs) -> None:
        text = "[blue][¡][/blue] " + content
        self.console.print(text, *args, **kwargs)

    def success(self, content: str, *args, **kwargs) -> None:
        text = "[green][√][/green] " + content
        self.console.print(text, *args, **kwargs)

    def warn(self, content: str, *args, **kwargs) -> None:
        text = "[yellow][‼️][/yellow] " + content
        self.console.print(text, *args, **kwargs)

    def error(self, content: str, *args, **kwargs) -> None:
        text = "[red][×][/red] " + content
        self.console.print(text, *args, **kwargs)

    def input(
        self,
        prompt: TextType = "",
        *,
        default_return="",
        assign_type=None,
        reject_message="",
        **kwargs,
    ) -> str:
        self.console.print(f"[gray][?][/gray] [white]{prompt}[/white]")
        while True:
            text = self.console.input("> ", **kwargs)
            if not text:
                self.info(
                    f"已使用默认设置: {default_return if default_return else '空'}"
                )
                return default_return

            if not assign_type:
                return text

            try:
                return assign_type(text)
            except Exception:
                self.warn(reject_message)


console = Console()
