# Тестовое задание:
Написать Python-скрипт, который преобразует входящий JSON в список с уникальными элементами. Учесть, что в JSON может быть большой уровень вложенности. JSON необходимо загружать из файла, путь к которому предаётся в аргументах запуска скрипта.

## Исходный JSON:
```json
{ "Users": [ { "id": 1, "employee": { "department": "tech", "name":
"Mark", "project": [ { "id": 2, "name": "Test", "status": "ok",
"mistakes": [] } ] } }, { "id": 2, "employee": { "department": "tech",
"name": "Alex", "project": [ { "id": 3, "name": "parser", "status":
"filed", "mistakes": [ 404, "IO error" ] } ] } } ] }
```
## Результат (порядок необязателен):
```json
['Users', 'id', 1, 'employee', 'department', 'tech', 'name', 'Mark',
'project', 2, 'Test', 'status', "ok", 'mistakes', 'Alex', 3, 'parser',
'filed', 404, 'IO error']
```

### Пример запуска скрипта
```shell
python converter.py --file in_data.json
```