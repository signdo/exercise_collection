use std::error::Error;

use ratatui::crossterm::event;
use ratatui::style::Stylize;
use ratatui::symbols::border;
use ratatui::widgets::block::Position;
use ratatui::widgets::{Block, Paragraph};
use ratatui::widgets::{block::Title, Widget};
use ratatui::prelude::*;


#[derive(Debug, Default)]
pub struct App {
    //resolution: (u32, u32),
    pub resolution: Rect,
    pub exit: bool,
}
impl App {
    fn resolution_to_string(&self) -> String {
        //format!("x: {}, y: {}", self.resolution.0, self.resolution.1)
        self.resolution.to_string()
    }
    pub fn detect_resolution(&mut self, frame: &Frame) {
        self.resolution = frame.size();
    }
    // fn exit(&mut self) -> result<(), box<dyn error>>{
    //     self.exit = true;
    //     ok(())
    // }
    pub fn handle_event(&mut self) -> Result<(), Box<dyn Error>> {
        match event::read()? {
            event::Event::Key(key_event) if key_event.kind == event::KeyEventKind::Press => match key_event.code {
                event::KeyCode::Char('q') | event::KeyCode::Char('Q')=> {
                    self.exit = true;
                    Ok(())
                }
                _ => Ok(())
            }
            _ => Ok(())
        }
    }
}

impl Widget for &App {
    fn render(self, area: ratatui::prelude::Rect, buf: &mut ratatui::prelude::Buffer)
        where
            Self: Sized {
        let title = Title::from("Resolution Detection".white().bold());
        let instructions = Title::from(Line::from(vec![
            "Press ".blue(),
            "<Q>".bold().red(),
            " to quit.".blue(),
        ]));

        let block = Block::bordered()
            .title(title.alignment(Alignment::Center))
            .title(instructions
                .alignment(Alignment::Center)
                .position(Position::Bottom)
            )
            .border_set(border::ROUNDED);

        let content_text = Text::from(vec![
            Line::from(vec![
                "Resolution: ".into(),
                self.resolution_to_string().yellow(),

            ])
        ]);

        Paragraph::new(content_text)
            .centered()
            .block(block)
            .render(area, buf);
    }
}
