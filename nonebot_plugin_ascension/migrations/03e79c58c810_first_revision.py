"""first revision

迁移 ID: 03e79c58c810
父迁移:
创建时间: 2024-07-24 16:19:04.094991

"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "03e79c58c810"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = ("nonebot_plugin_ascension",)
depends_on: str | Sequence[str] | None = None


def upgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "backpack",
        sa.Column("user_id", sa.String(), nullable=False),
        sa.Column("goods_id", sa.Integer(), nullable=False),
        sa.Column("goods_name", sa.String(), nullable=False),
        sa.Column("goods_type", sa.String(), nullable=False),
        sa.Column("goods_amount", sa.Integer(), nullable=False),
        sa.Column("bind_amount", sa.Integer(), nullable=False),
        sa.Column("create_time", sa.DateTime(), nullable=False),
        sa.Column("update_time", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("user_id", name=op.f("pk_backpack")),
        info={"bind_key": "nonebot_plugin_ascension"},
    )
    op.create_table(
        "buff",
        sa.Column("user_id", sa.String(), nullable=False),
        sa.Column("main_buff", sa.Integer(), nullable=False),
        sa.Column("sec_buff", sa.Integer(), nullable=False),
        sa.Column("sub_buff", sa.Integer(), nullable=False),
        sa.Column("dharma_buff", sa.Integer(), nullable=False),
        sa.Column("armor_buff", sa.Integer(), nullable=False),
        sa.Column("atk_buff", sa.Integer(), nullable=False),
        sa.Column("blessed_spot", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("user_id", name=op.f("pk_buff")),
        info={"bind_key": "nonebot_plugin_ascension"},
    )
    op.create_table(
        "sect",
        sa.Column("sect_id", sa.String(), nullable=False),
        sa.Column("sect_name", sa.String(), nullable=False),
        sa.Column("sect_owner", sa.String(), nullable=False),
        sa.Column("sect_scale", sa.Integer(), nullable=True),
        sa.Column("sect_stone_amount", sa.Integer(), nullable=False),
        sa.Column("sect_fairyland", sa.Integer(), nullable=True),
        sa.Column("sect_materials", sa.Integer(), nullable=False),
        sa.Column("main_buff", sa.String(), nullable=True),
        sa.Column("sec_buff", sa.String(), nullable=True),
        sa.Column("elixir_room_level", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("sect_id", name=op.f("pk_sect")),
        info={"bind_key": "nonebot_plugin_ascension"},
    )
    op.create_table(
        "user",
        sa.Column("user_id", sa.String(), nullable=False),
        sa.Column("user_name", sa.String(length=15), nullable=False),
        sa.Column("user_title", sa.String(), nullable=True),
        sa.Column("root", sa.String(), nullable=False),
        sa.Column("root_type", sa.String(), nullable=False),
        sa.Column("level", sa.String(), nullable=False),
        sa.Column("stone", sa.Integer(), nullable=False),
        sa.Column("power", sa.Integer(), nullable=False),
        sa.Column("user_stamina", sa.Integer(), nullable=False),
        sa.Column("exp", sa.Integer(), nullable=False),
        sa.Column("sect_id", sa.String(), nullable=True),
        sa.Column("sect_position", sa.String(), nullable=True),
        sa.Column("sect_task", sa.Integer(), nullable=False),
        sa.Column("sect_contribution", sa.Integer(), nullable=False),
        sa.Column("sect_elixir_get", sa.Integer(), nullable=False),
        sa.Column("is_sign", sa.Boolean(), nullable=False),
        sa.Column("is_beg", sa.Boolean(), nullable=False),
        sa.Column("is_ban", sa.Boolean(), nullable=False),
        sa.Column("level_up_cd", sa.DateTime(), nullable=True),
        sa.Column("level_up_rate", sa.Integer(), nullable=True),
        sa.Column("work_refresh_times", sa.Integer(), nullable=False),
        sa.Column("hp", sa.Integer(), nullable=False),
        sa.Column("mp", sa.Integer(), nullable=False),
        sa.Column("atk", sa.Integer(), nullable=False),
        sa.Column("atk_practice", sa.Integer(), nullable=False),
        sa.Column("blessed_spot_name", sa.String(), nullable=True),
        sa.Column("blessed_spot_flag", sa.Integer(), nullable=False),
        sa.Column("create_time", sa.DateTime(), nullable=False),
        sa.Column("last_check_time", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("user_id", "user_name", name=op.f("pk_user")),
        sa.UniqueConstraint("user_id"),
        sa.UniqueConstraint("user_name"),
        info={"bind_key": "nonebot_plugin_ascension"},
    )
    op.create_table(
        "user_cd",
        sa.Column("user_id", sa.String(), nullable=False),
        sa.Column(
            "status",
            sa.Enum(
                "NONE",
                "MEDITATING",
                "WORKING",
                "EXPLORING",
                "PRACTICING",
                name="userstatus",
            ),
            nullable=False,
        ),
        sa.Column("create_time", sa.DateTime(), nullable=False),
        sa.Column("scheduled_time", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("user_id", name=op.f("pk_user_cd")),
        info={"bind_key": "nonebot_plugin_ascension"},
    )
    op.drop_table("wakatime")
    # ### end Alembic commands ###


def downgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "wakatime",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("platform", sa.VARCHAR(), nullable=False),
        sa.Column("access_token", sa.VARCHAR(), nullable=False),
        sa.Column("refresh_token", sa.VARCHAR(), nullable=False),
        sa.PrimaryKeyConstraint("id", name="pk_wakatime"),
    )
    op.drop_table("user_cd")
    op.drop_table("user")
    op.drop_table("sect")
    op.drop_table("buff")
    op.drop_table("backpack")
    # ### end Alembic commands ###