# Pydantic is fundamentally:
# A runtime data validation + parsing system built around Python type hints.
#
# Python type hints alone do NOTHING at runtime.
#
# This is valid:
#
# def f(x: int):
#     return x
#
# f("hello")
#
# Python will happily allow it.
#
# Pydantic makes type hints:
# executable runtime contracts.


# from pydantic import BaseModel
#
#
# class User(BaseModel):
#     name: str
#     age: int
#
#
# u = User(name="Alice", age="25")

# Notice:
# "25" became 25.
#
# Pydantic is not merely validation.
# It is:
# parsing + normalization.

# Pydantic models are basically:
# Typed schema objects with runtime guarantees


# Strict vs Permissive Validation
# Default Pydantic behavior is somewhat permissive.
# Example "25" was parsed and corrected to 25

# Strict Mode
# from pydantic import StrictInt
#
# class User(BaseModel):
#     age: StrictInt


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int


@app.post("/users")
async def create_user(user: User):
    return user


# Pydantic also handles serialization and deserialization
# user.model_dump

# Field Constraints
#
# Example:
# from pydantic import BaseModel, Field
#
# class User(BaseModel):
#     age: int = Field(gt=0, lt=150)


# Validators
# Custom logic:
#
# from pydantic import field_validator
#
# class User(BaseModel):
#     name: str
#
#     @field_validator("name")
#     def validate_name(cls, v):
#         if len(v) < 3:
#             raise ValueError("too short")
#         return v
#
# This lets you encode:
# domain invariants,
# business constraints.



# Pydantic v1 vs v2
# Pydantic v2 introduced:
#
# major performance rewrite,
# Rust-powered core,
# new validation engine,
# different APIs.
#
# Core runtime now uses:
# pydantic-core
# written in Rust for huge speedups.


# External Data
#     ↓
# Pydantic Model
#     ↓
# Validated Internal Representation
#     ↓
# Business Logic
