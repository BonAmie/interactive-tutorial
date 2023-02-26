use userbd

Create table [Users]
(
  [Id] INT Primary key identity,
  [Name] nvarchar(30),
  [Class] int,
  [progress] int,
)

INSERT [Users] Values
('Num1', 1, 67),
('Num2', 4, 34),
('Num3', 3, 12)

Select * from [Users]