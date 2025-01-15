from ruamel.yaml import YAML
from pydantic import Field, BaseModel
from nonebot_plugin_uninfo import Session
from ruamel.yaml.comments import CommentedMap

from .path import BOT_DIR
from .console import console
from .configs import (
    BegConfig,
    BetConfig,
    SectConfig,
    BasicConfig,
    StealConfig,
    SignInConfig,
    ClosingConfig,
    LevelUpConfig,
    RebirthConfig,
    SessionConfig,
    StaminaConfig,
)

yaml = YAML(typ="unsafe", pure=True)
yaml.default_flow_style = False
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.representer.add_representer(
    CommentedMap, lambda dumper, data: dumper.represent_dict(data)
)


class MarisaConfig(BaseModel):
    basic: BasicConfig = Field(default_factory=BasicConfig, alias="基础")
    sign_in: SignInConfig = Field(default_factory=SignInConfig, alias="签到")
    stamina: StaminaConfig = Field(default_factory=StaminaConfig, alias="体力")
    steal: StealConfig = Field(default_factory=StealConfig, alias="偷灵石")
    level_up: LevelUpConfig = Field(default_factory=LevelUpConfig, alias="突破")
    closing: ClosingConfig = Field(default_factory=ClosingConfig, alias="闭关")
    rebirth: RebirthConfig = Field(default_factory=RebirthConfig, alias="重入仙途")
    bet: BetConfig = Field(default_factory=BetConfig, alias="金银阁")
    beg: BegConfig = Field(default_factory=BegConfig, alias="仙途奇缘")
    sect: SectConfig = Field(default_factory=SectConfig, alias="宗门")
    session_config: dict[int, SessionConfig] = Field(
        default_factory=dict,
        alias="分群管理",
    )


class ConfigManager:
    def __init__(self) -> None:
        self.file_path = BOT_DIR / "marisa.yaml"
        if self.file_path.exists():
            is_continue = "y"
            self.config = MarisaConfig.model_validate(
                obj=yaml.load(self.file_path.read_text(encoding="utf-8"))
            )
        else:
            self.config = MarisaConfig()
            console.info("欢迎使用 Marisa Bot")
            console.info(f"已为您生成后台管理密码: {self.config.basic.webui_password}")
            is_continue = console.input("输入 y/N 以确定是否继续")
            if is_continue.lower() == "n":
                console.info(content="已退出程序")

        self.save()
        if is_continue and is_continue.lower() == "n":
            quit()

    def save(self) -> None:
        commented_data = self._add_comments(self.config)
        with self.file_path.open("w", encoding="utf-8") as f:
            yaml.dump(commented_data, f)

    def get_config(self) -> MarisaConfig:
        return self.config

    def get_session_config(self, session: Session) -> SessionConfig:
        session_id = int(session.scene.id)
        if session.scene.id not in self.config.session_config:
            self.config.session_config[session_id] = SessionConfig()
            self.save()
        return self.config.session_config[session_id]

    def _add_comments(self, model: BaseModel) -> CommentedMap:
        # TODO: fix comments not working

        data = CommentedMap()
        for field_name, field in model.model_fields.items():
            alias = field.alias or field_name
            value = getattr(model, field_name)

            if isinstance(value, BaseModel):
                value = self._add_comments(value)

            data[alias] = value
            if field.description:
                data.yaml_set_comment_before_after_key(
                    key=alias, after=field.description, after_indent=2
                )

        return data

    @property
    def config_list(self) -> list[str]:
        return list(self.config.model_dump(by_alias=True).keys())


config_manager = ConfigManager()
config: MarisaConfig = config_manager.get_config()
