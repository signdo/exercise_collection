use std::io;

use rand::Rng;
use ratatui::prelude::*;
use ratatui::widgets::block::Position;
use ratatui::{
    crossterm::event::{self, Event, KeyCode, KeyEventKind},
    layout::{Alignment, Rect},
    symbols::border,
    text::Text,
    widgets::{block::Title, Block, Paragraph, Widget}
};

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
struct Point {
    x: u16,
    y: u16,
}

impl Point {
    fn new(x: u16, y: u16) -> Point {
        Point {
            x, y,
        }
    }
}

pub struct App {
    cursor_position: Point,
    char_position: Point,
    frame_size_limit: Point,
    pub exit: bool,
}

impl Default for App {
    fn default() -> Self {
        App {
            cursor_position: Point::new(0, 0),
            char_position: Point::new(1, 0),
            frame_size_limit: Point::new(0, 0),
            exit: false,
        }
    }
}

impl App {
    pub fn set_frame_size_limit(&mut self, rect: Rect) {
        self.frame_size_limit.x = rect.width;
        self.frame_size_limit.y = rect.height;
    }
    pub fn update_char_position(&mut self) {
        while self.char_position.eq(&self.cursor_position) {
            let x = rand::thread_rng().gen_range(0..(self.frame_size_limit.x - 2));
            let y = rand::thread_rng().gen_range(0..(self.frame_size_limit.y - 2));
            self.char_position = Point::new(x, y);
        }
    }
    pub fn handle_event(&mut self) -> Result<(), io::Error>{
        match event::read()? {
            Event::Key(event_key) if event_key.kind == KeyEventKind::Press => match event_key.code {
                KeyCode::Up | KeyCode::Char('k') | KeyCode::Char('w') => {
                    if self.cursor_position.y > 0 {
                        self.cursor_position.y -= 1;
                    }
                }
                KeyCode::Down | KeyCode::Char('j') | KeyCode::Char('s') => {
                    if self.cursor_position.y < self.frame_size_limit.y - 3 {
                        self.cursor_position.y += 1;
                    }
                }
                KeyCode::Left | KeyCode::Char('h') | KeyCode::Char('a') => {
                    if self.cursor_position.x > 0 {
                        self.cursor_position.x -= 1;
                    }
                }
                KeyCode::Right | KeyCode::Char('l') | KeyCode::Char('d') => {
                    if self.cursor_position.x < self.frame_size_limit.x - 3 {
                        self.cursor_position.x += 1;
                    }
                }
                KeyCode::Esc | KeyCode::Char('q') | KeyCode::Char('Q') => {
                    self.exit = true;
                }
                _ => {}
            }
            _ => {}
        }
        Ok(())
    }
}

impl Widget for &App {
    fn render(self, area: ratatui::prelude::Rect, buf: &mut ratatui::prelude::Buffer)
where
        Self: Sized {

        let title = Title::from(" HJKL Run! ".bold());
        let resolution = Title::from(format!(
            " [resolution: {}, {}] ",
            self.frame_size_limit.x,
            self.frame_size_limit.y
        ));

        // draw a black rectangle as character background
        let mut blank_rect = Text::from(
            vec![
                Line::from(vec![
                    Span::from(" ");
                    (self.frame_size_limit.x - 2) as usize
                ]);
                (self.frame_size_limit.y - 2) as usize
            ]
        );

        // change cursor style
        let cursor = &mut blank_rect.lines[self.cursor_position.y as usize].spans[self.cursor_position.x as usize];
        cursor.style = Style::new().on_yellow();

        let cursor_position = Title::from(format!(
            " [cursor: {}, {}] ",
            self.cursor_position.x,
            self.cursor_position.y
        ));


        // change char style
        let char_code = &mut blank_rect.lines[self.char_position.y as usize].spans[self.char_position.x as usize];
        char_code.style = Style::new().on_green();

        let char_position = Title::from(format!(
            " [char: {}, {}] ",
            self.char_position.x,
            self.char_position.y
        ));

        let block = Block::bordered()
            .title(title.alignment(Alignment::Left))
            .title(resolution
                .alignment(Alignment::Right)
                .position(Position::Bottom)
            )
            .title(cursor_position
                .alignment(Alignment::Left)
                .position(Position::Bottom)
            )
            .title(char_position
                .alignment(Alignment::Center)
                .position(Position::Bottom)
            )
            .border_set(border::DOUBLE);

        Paragraph::new(blank_rect)
            .block(block)
            .render(area, buf);
    }
}
