# Лабораторная №1  

Примечание: задание сформулировано для проекта по курсу БД, как самого недавнего для студентов. В качестве
объекта тестирования может быть выбран любой многокомпонентный проект, написанный или изученный студентом.  

### Задание:
1. Написать unit-тесты для компонентов доступа к данным и бизнес логики курсовой работы по БД

### Требования:
1. Требуемое покрытие тестами: **один класс - как минимум один test suite с как минимум тремя тестами**; если проект
для тестирования выполнен не в объектном стиле -- то необходимо выделить модули исходя из логической
структуры программы (один файл с функциями в условном Python-проекте может в себе содержать несколько
полноценных модулей, которые при ОО подходе были бы отдельными классами)
2. Должны быть представлены тесты **как в классическом так и в “Лондонском” варианте** с обоснованием, почему
выбран конкретный подход; допустимо представить один и тот же тест в обоих вариантах для сравнения
3. Должны быть представлены варианты использования **mock \ stub**
4. Должна быть соблюдена структура **Arrange-Act-Assert** для каждого теста c использованием fixture и остальных
классов\методов хелперов
5. Должны быть представлены тесты с использованием паттерна **Data Builder** (Object Mother -- опционально)
6. Должен быть **настроен локальный запуск тестов** в среде разработки
7. Защита от регрессии, устойчивость к рефакторингу и легкость поддержки -- базовые принципы, которым стоит
следовать